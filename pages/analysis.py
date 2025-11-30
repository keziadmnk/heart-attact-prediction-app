# pages/analysis.py
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from helpers import (
    require_clean_data,
    plot_confusion_matrix,
    plot_feature_importance,
    TARGET_COL,
)


def show_analysis():
    # Judul halaman Analisis / Training model
    st.title("Training Model & Evaluasi")

    # Pastikan data hasil preprocessing sudah tersedia,
    # kalau belum, fungsi require_clean_data() akan menampilkan warning dan menghentikan eksekusi
    require_clean_data()
    df_clean = st.session_state["clean_df"]

    # Card penjelasan singkat tentang apa yang dilakukan di halaman ini
    st.markdown(
        """
        <div class="data-card">
            <p style="font-size: 1rem; color: #555;">
                Pada halaman ini, model <strong>Random Forest Classifier</strong> akan dilatih menggunakan 
                data hasil preprocessing. Dataset akan dibagi menjadi data training dan testing secara otomatis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------
    # Pengaturan Model
    # -----------------------------------------
    # Bagian ini dibungkus dalam expander agar tampilan lebih rapi.
    # User bisa mengatur hyperparameter Random Forest dan proporsi data testing.
    with st.expander("⚙️ Pengaturan Model (Opsional)"):
        col1, col2 = st.columns(2)
        with col1:
            # Slider untuk mengatur jumlah tree dalam Random Forest
            n_estimators = st.slider(
                "🌳 Jumlah Trees (n_estimators)",
                50,
                500,
                200,
                step=50,
                help="Jumlah pohon keputusan dalam Random Forest",
            )
        with col2:
            # Slider untuk mengatur proporsi data testing (sisa otomatis jadi data training)
            test_size = st.slider(
                "📊 Proporsi Data Testing",
                0.1,
                0.4,
                0.2,
                step=0.05,
                help="Persentase data yang digunakan untuk testing",
            )

    # -----------------------------------------
    # Tombol Training
    # -----------------------------------------
    # Saat tombol ini diklik, proses training model akan dijalankan
    if st.button("Mulai Training Model", key="run_training"):
        # Tampilkan spinner selama proses training berlangsung
        with st.spinner("⏳ Sedang melatih model Random Forest..."):
            # X = fitur, y = label/target
            X = df_clean[st.session_state["features"]]
            y = df_clean[TARGET_COL]

            # Bagi data menjadi train dan test sesuai test_size
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42, stratify=y
            )

            # Inisialisasi model Random Forest dengan parameter yang dipilih user
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                random_state=42,
                class_weight="balanced",
                n_jobs=-1,
            )

            # Latih model dengan data training
            model.fit(X_train, y_train)
            # Prediksi label untuk data testing
            y_pred = model.predict(X_test)

            # Hitung metrik evaluasi
            acc = accuracy_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)

            # Simpan semua hasil ke session_state supaya bisa dipakai kembali
            st.session_state["rf_model"] = model
            st.session_state["acc"] = acc
            st.session_state["cm"] = cm
            st.session_state["report"] = report
            st.session_state["X_cols"] = X.columns.tolist()

        # Notifikasi bahwa training selesai
        st.success("✅ Training model selesai!")
        # Rerun halaman supaya blok di bawah (hasil evaluasi) langsung muncul dengan data terbaru
        st.rerun()  # agar hasil tampil di blok bawah

    # -------------------------------------------------
    # BLOK INI SELALU TAMPIL jika model sudah tersedia
    # -------------------------------------------------
    # Jadi meskipun user pindah halaman lalu balik, hasil model tetap ada selama session belum di-reset
    if st.session_state.get("rf_model") is not None:

        # Ambil kembali objek model dan metrik evaluasi dari session_state
        model = st.session_state["rf_model"]
        acc = st.session_state["acc"]
        cm = st.session_state["cm"]
        report = st.session_state["report"]
        X_cols = st.session_state["X_cols"]

        st.markdown("### 📊 Hasil Evaluasi Model")

        # Tampilkan ringkasan metrik dalam bentuk cards
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            # Akurasi dalam persen
            st.metric("🎯 Akurasi", f"{acc*100:.2f}%")
        with c2:
            # Jumlah tree yang digunakan (diambil dari slider terakhir yang diset)
            st.metric("🌳 Trees", f"{n_estimators}")
        with c3:
            # Info singkat bahwa pembagian train ditentukan otomatis dari test_size
            st.metric("📊 Training", f"(otomatis)")
        with c4:
            # Info singkat bahwa pembagian test juga otomatis
            st.metric("📊 Testing", f"(otomatis)")

        # Confusion matrix untuk melihat distribusi prediksi benar/salah per kelas
        st.markdown("### 📊 Confusion Matrix")
        plot_confusion_matrix(cm, labels=["Tidak Serangan (0)", "Serangan Jantung (1)"])

        # Classification report (precision, recall, f1-score per kelas)
        st.markdown("### 📈 Classification Report")
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df.style.background_gradient(cmap="Reds"), use_container_width=True)

        # Feature importance dari model Random Forest
        st.markdown("### 🎯 Feature Importance")
        plot_feature_importance(model, X_cols)

        # -----------------------------------------
        # TOMBOL NAVIGASI
        # -----------------------------------------
        # Tombol Previous di ujung kiri dan Next di ujung kanan, sejajar dengan konten
        col_prev, col_spacer, col_next = st.columns([3, 6, 3], gap="large")
        
        with col_prev:
            # Tombol Previous untuk kembali ke halaman Preprocessing
            if st.button("< Previous", key="goto_preprocessing", use_container_width=False):
                st.session_state["page"] = "Preprocessing Data"
                st.rerun()
        
        with col_spacer:
            # Spacer kosong
            st.empty()
        
        with col_next:
            # Kalau ditekan, langsung mengubah halaman ke "Data Visualization"
            if st.button("Next >", key="goto_viz", use_container_width=False):
                st.session_state["page"] = "Data Visualization"
                st.rerun()
        
        # Inject JavaScript untuk menambahkan class ke button setelah di-render
        st.markdown("""
        <script>
        function styleNavButtons() {
            const buttons = document.querySelectorAll('.stButton > button');
            buttons.forEach(button => {
                const text = button.textContent.trim();
                if (text.includes('Previous')) {
                    button.classList.add('nav-button-prev');
                    button.style.whiteSpace = 'nowrap';
                    button.style.textAlign = 'center';
                } else if (text.includes('Next')) {
                    button.classList.add('nav-button-next');
                    button.style.whiteSpace = 'nowrap';
                    button.style.textAlign = 'center';
                }
            });
        }
        // Jalankan setelah DOM siap
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', styleNavButtons);
        } else {
            styleNavButtons();
        }
        // Jalankan lagi setelah Streamlit selesai render
        setTimeout(styleNavButtons, 100);
        // Jalankan lagi setelah delay lebih lama untuk memastikan
        setTimeout(styleNavButtons, 500);
        </script>
        """, unsafe_allow_html=True)

        # Info tambahan bahwa model sudah siap dipakai untuk menu Prediction
        st.success("✅ Model sudah tersedia dan siap digunakan untuk prediksi.")
