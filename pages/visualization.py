# pages/visualization.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import helper functions dan konstanta dari helpers.py
from helpers import (
    require_clean_data,           # memastikan data hasil preprocessing sudah tersedia
    generate_pdf_visualizations,  # fungsi untuk membuat file PDF berisi beberapa plot
    plot_feature_importance,      # fungsi untuk menampilkan grafik feature importance
    TARGET_COL,                   # nama kolom target (heart_attack)
)


def show_visualization():
    # Judul halaman utama
    st.title("Visualisasi Data")

    # Pastikan data hasil preprocessing sudah ada di session_state
    require_clean_data()
    # Ambil DataFrame yang sudah dibersihkan
    df = st.session_state["clean_df"]

    # Membuat 4 tab untuk memisahkan jenis visualisasi
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📈 Distribusi Data", "🔥 Korelasi Fitur", "🎯 Feature Importance", "💾 Export PDF"]
    )

    # ==========================================================
    # --- TAB 1: Distribusi Data & Proporsi Serangan Jantung ---
    # ==========================================================
    with tab1:
        st.markdown("### 📊 Distribusi Usia")

        # Membuat figure baru untuk histogram usia
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        # Plot distribusi usia menggunakan seaborn
        sns.histplot(df["age"], bins=20, kde=True, ax=ax1, color="#8B0000")
        ax1.set_xlabel("Usia (tahun)", fontsize=12, fontweight="bold")
        ax1.set_ylabel("Frekuensi", fontsize=12, fontweight="bold")
        ax1.set_title("Distribusi Usia Pasien", fontsize=14, fontweight="bold", pad=15)
        plt.tight_layout()
        # Tampilkan plot ke halaman Streamlit
        st.pyplot(fig1)

        st.markdown("### 🏥 Proporsi Serangan Jantung")

        # Membagi layout menjadi dua kolom: kiri (grafik bar), kanan (metrik)
        col1, col2 = st.columns([2, 1])
        with col1:
            # Figure untuk bar chart jumlah kasus serangan / tidak
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            # Menghitung jumlah setiap kelas target
            heart_counts = df[TARGET_COL].value_counts()
            colors = ["#28a745", "#8B0000"]
            # Membuat bar chart
            bars = ax2.bar(heart_counts.index, heart_counts.values, color=colors)
            ax2.set_xticks([0, 1])
            ax2.set_xticklabels(["Tidak (0)", "Ya (1)"], fontsize=11, fontweight="bold")
            ax2.set_ylabel("Jumlah", fontsize=12, fontweight="bold")
            ax2.set_title(
                "Distribusi Label Serangan Jantung", fontsize=14, fontweight="bold", pad=15
            )

            # Menambahkan label angka di atas setiap bar
            for bar in bars:
                height = bar.get_height()
                ax2.text(
                    bar.get_x() + bar.get_width() / 2.0,  # posisi X di tengah bar
                    height,                               # posisi Y di atas bar
                    f"{int(height)}",                     # teks = nilai integer
                    ha="center",
                    va="bottom",
                    fontsize=11,
                    fontweight="bold",
                )
            plt.tight_layout()
            st.pyplot(fig2)

        with col2:
            # Menampilkan metrik jumlah kasus tidak serangan jantung
            st.metric(
                "❌ Tidak Serangan",
                f"{heart_counts.get(0, 0):,}",
                help="Jumlah kasus tanpa serangan jantung",
            )
            # Menampilkan metrik jumlah kasus serangan jantung
            st.metric(
                "⚠️ Serangan Jantung",
                f"{heart_counts.get(1, 0):,}",
                help="Jumlah kasus serangan jantung",
            )
            # Menghitung rasio kasus serangan jantung terhadap kasus tidak serangan
            ratio = (
                (heart_counts.get(1, 0) / heart_counts.get(0, 1)) * 100
                if heart_counts.get(0, 1) > 0
                else 0
            )
            st.metric("📊 Rasio", f"{ratio:.1f}%", help="Persentase kasus serangan jantung")

    # =====================================
    # --- TAB 2: Heatmap Korelasi Fitur ---
    # =====================================
    with tab2:
        st.markdown("### 🔥 Heatmap Korelasi Fitur")

        # Figure untuk heatmap korelasi
        fig3, ax3 = plt.subplots(figsize=(12, 10))
        # Menghitung matriks korelasi antar semua kolom numerik
        corr = df.corr()
        # Membuat mask segitiga atas agar heatmap lebih rapi
        mask = np.triu(np.ones_like(corr, dtype=bool))
        # Plot heatmap menggunakan seaborn
        sns.heatmap(
            corr,
            mask=mask,
            cmap="Reds",
            ax=ax3,
            annot=False,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.8},
        )
        ax3.set_title("Heatmap Korelasi Antar Fitur", fontsize=14, fontweight="bold", pad=20)
        plt.tight_layout()
        st.pyplot(fig3)

        st.markdown("### 🔍 Top 10 Korelasi dengan Target")

        # Mengambil korelasi absolut semua fitur terhadap kolom target
        target_corr = (
            corr[TARGET_COL]                 # ambil kolom korelasi dengan target
            .drop(TARGET_COL)                # hilangkan korelasi target dengan dirinya sendiri
            .abs()                           # ambil nilai absolut
            .sort_values(ascending=False)    # urutkan dari terbesar ke terkecil
            .head(10)                        # ambil 10 fitur teratas
        )

        # Figure untuk bar chart top 10 korelasi
        fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
        colors_corr = plt.cm.Reds(np.linspace(0.4, 0.8, len(target_corr)))
        ax_corr.barh(target_corr.index, target_corr.values, color=colors_corr)
        ax_corr.set_xlabel("Korelasi (Absolut)", fontsize=12, fontweight="bold")
        ax_corr.set_title(
            "Top 10 Fitur Berkorelasi dengan Serangan Jantung",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        plt.tight_layout()
        st.pyplot(fig_corr)

    # ========================================
    # --- TAB 3: Feature Importance Model ---
    # ========================================
    with tab3:
        st.markdown("### 🎯 Feature Importance (Random Forest)")

        # Pastikan model sudah ditraining terlebih dahulu
        if st.session_state.get("rf_model") is not None:
            # Tampilkan plot feature importance dengan helper
            plot_feature_importance(st.session_state["rf_model"], st.session_state["features"])

            # Ambil nilai feature_importances_ dari model
            importances = st.session_state["rf_model"].feature_importances_

            # Membentuk DataFrame yang berisi nama fitur dan importance-nya
            feature_imp_df = (
                pd.DataFrame(
                    {
                        "Fitur": st.session_state["features"],
                        "Importance": importances,
                    }
                )
                .sort_values("Importance", ascending=False)  # urutkan dari yang paling penting
            )

            st.markdown("### 📋 Tabel Feature Importance")
            # Tampilkan tabel dengan background gradasi warna
            st.dataframe(
                feature_imp_df.style.background_gradient(cmap="Reds"),
                use_container_width=True,
            )
        else:
            # Jika model belum tersedia, tampilkan peringatan
            st.warning(
                "⚠️ Model belum dilatih. Silakan lakukan training di menu **Analisis Data**."
            )

    # =====================================
    # --- TAB 4: Export Visualisasi PDF ---
    # =====================================
    with tab4:
        st.markdown("### 📥 Export Visualisasi ke PDF")
        st.info("💾 Unduh semua visualisasi dalam satu file PDF untuk dokumentasi atau presentasi.")

        # Tombol untuk generate file PDF berisi beberapa plot
        if st.button("📄 Generate PDF", use_container_width=False):
            with st.spinner("⏳ Sedang membuat file PDF..."):
                # Panggil helper untuk menghasilkan PDF (mengembalikan buffer BytesIO)
                buf = generate_pdf_visualizations(df, st.session_state.get("rf_model"))

            st.success("✅ File PDF berhasil dibuat!")
            # Tombol download PDF
            st.download_button(
                label="📥 Unduh Visualisasi PDF",
                data=buf,
                file_name="visualisasi_heart_attack_indonesia.pdf",
                mime="application/pdf",
                use_container_width=False,
            )
    
    st.markdown("---")
    
    # Tombol Previous di ujung kiri dan Next di ujung kanan, sejajar dengan konten
    # Menggunakan rasio kolom yang sama dengan Preprocessing.py (3:6:3)
    col_prev, col_spacer, col_next = st.columns([3, 6, 3], gap="large") 
    
    # Tombol Previous (Abu-abu)
    with col_prev:
        # Tambahkan class nav-button-prev via JavaScript (disediakan di akhir file ini)
        if st.button("< Previous", key="goto_analysis_prev", use_container_width=False):
            st.session_state["page"] = "Analisis Data" # Kembali ke halaman sebelumnya
            st.rerun()
            
    with col_spacer:
        st.empty() # Spacer kosong
        
    # Tombol Next (Merah)
    with col_next:
        # Tombol Next untuk berpindah ke halaman Prediction
        if st.button("Next >", key="goto_prediction_next", use_container_width=False):
            st.session_state["page"] = "Prediction" # Lanjut ke halaman berikutnya
            st.rerun()

    # Inject JavaScript untuk menambahkan class CSS ke tombol setelah di-render
    # (Ini diambil dari pages/preprocessing.py)
    st.markdown("""
    <script>
    function styleNavButtons() {
        const buttons = document.querySelectorAll('.stButton > button');
        buttons.forEach(button => {
            const text = button.textContent.trim();
            // Menambahkan kelas CSS berdasarkan teks tombol
            if (text.includes('Previous')) {
                button.classList.add('nav-button-prev');
                button.style.whiteSpace = 'nowrap';
                button.style.textAlign = 'center';
            } else if (text.includes('Next')) {
                button.classList.add('nav-button-next');
                button.style.whiteSpace = 'nowrap';
                button.style.textAlign = 'center';
            } else if (text.includes('Prediction')) { /* Tambahan untuk tombol 'Prediction' */
                button.classList.add('nav-button-next');
                button.style.whiteSpace = 'nowrap';
                button.style.textAlign = 'center';
            }
        });
    }
    // Jalankan setelah DOM siap dan setelah Streamlit merender ulang
    setTimeout(styleNavButtons, 100);
    setTimeout(styleNavButtons, 500);
    </script>
    """, unsafe_allow_html=True)
