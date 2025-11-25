# pages/prediction.py
import streamlit as st
import pandas as pd

from helpers import require_model  # fungsi helper untuk memastikan model sudah tersedia di session_state


def show_prediction():
    # Judul utama halaman prediksi individu
    st.title("🩺 Prediksi Risiko Serangan Jantung")

    # Pastikan model sudah dilatih, kalau belum user diarahkan untuk training dulu
    require_model()

    # Card penjelasan singkat tentang fungsi halaman ini
    st.markdown(
        """
        <div class="data-card">
            <p style="font-size: 1rem; color: #555;">
                Masukkan data kesehatan individu di bawah ini untuk memprediksi risiko serangan jantung 
                berdasarkan model Random Forest yang sudah dilatih.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------
    # FORM INPUT DATA PASIEN
    # -----------------------------------------
    # Form memastikan input dikirim sekaligus saat tombol submit ditekan
    with st.form("form_prediksi"):
        st.markdown("### 📋 Data Kesehatan Pasien")

        # Dua kolom: kiri (data numerik utama), kanan (status kesehatan & gaya hidup)
        col1, col2 = st.columns(2)

        # -----------------------------
        # KOLOM KIRI: Usia & Tekanan Darah + Profil Lipid
        # -----------------------------
        with col1:
            st.markdown("#### 👤 Data Demografis & Tekanan Darah")
            # Input usia pasien
            age = st.number_input(
                "Usia (tahun)",
                min_value=18,
                max_value=100,
                value=40,
                help="Masukkan usia dalam tahun",
            )
            # Tekanan darah sistolik
            systolic = st.number_input(
                "Tekanan Darah Sistolik (mmHg)",
                min_value=80,
                max_value=250,
                value=120,
                help="Tekanan darah saat jantung memompa",
            )
            # Tekanan darah diastolik
            diastolic = st.number_input(
                "Tekanan Darah Diastolik (mmHg)",
                min_value=50,
                max_value=150,
                value=80,
                help="Tekanan darah saat jantung rileks",
            )

            st.markdown("#### 💉 Data Kolesterol & Gula Darah")
            # Kolesterol total
            cholesterol_level = st.number_input(
                "Kolesterol Total (mg/dL)", min_value=80, max_value=400, value=200
            )
            # HDL (kolesterol baik)
            hdl = st.number_input(
                "Kolesterol HDL (mg/dL)",
                min_value=10,
                max_value=120,
                value=40,
                help="Kolesterol baik",
            )
            # LDL (kolesterol jahat)
            ldl = st.number_input(
                "Kolesterol LDL (mg/dL)",
                min_value=10,
                max_value=300,
                value=120,
                help="Kolesterol jahat",
            )
            # Trigliserida
            triglycerides = st.number_input(
                "Trigliserida (mg/dL)", min_value=30, max_value=600, value=150
            )
            # Gula darah puasa
            fasting_blood_sugar = st.number_input(
                "Gula Darah Puasa (mg/dL)", min_value=50, max_value=400, value=100
            )

        # -----------------------------
        # KOLOM KANAN: Kondisi Kesehatan & Gaya Hidup
        # -----------------------------
        with col2:
            st.markdown("#### 🏥 Kondisi Kesehatan")
            # Status hipertensi (0 / 1)
            hypertension = st.selectbox(
                "Hipertensi",
                ["Tidak (0)", "Ya (1)"],
                help="Apakah memiliki riwayat hipertensi?",
            )
            # Status diabetes (0 / 1)
            diabetes = st.selectbox(
                "Diabetes", ["Tidak (0)", "Ya (1)"], help="Apakah memiliki riwayat diabetes?"
            )
            # Status obesitas (0 / 1)
            obesity = st.selectbox(
                "Obesitas", ["Tidak (0)", "Ya (1)"], help="Apakah termasuk kategori obesitas?"
            )
            # Riwayat penyakit jantung sebelumnya (0 / 1)
            prev_hd = st.selectbox(
                "Riwayat Penyakit Jantung",
                ["Tidak (0)", "Ya (1)"],
                help="Apakah pernah mengalami penyakit jantung sebelumnya?",
            )
            # Lingkar pinggang sebagai indikator risiko
            waist = st.number_input(
                "Lingkar Pinggang (cm)",
                min_value=50,
                max_value=200,
                value=85,
                help="Ukuran lingkar pinggang dalam cm",
            )

            st.markdown("#### 🚭 Gaya Hidup")
            # Status merokok (dikodekan 0/1/2)
            smoking = st.selectbox(
                "Status Merokok",
                ["Tidak Pernah (0)", "Mantan Perokok (1)", "Aktif Merokok (2)"],
            )
            # Tingkat aktivitas fisik (dikodekan 0/1/2)
            physical_activity = st.selectbox(
                "Aktivitas Fisik",
                ["Rendah (0)", "Sedang (1)", "Tinggi (2)"],
                help="Tingkat aktivitas fisik sehari-hari",
            )

        # Garis pemisah dan tombol submit form
        st.markdown("---")
        submitted = st.form_submit_button("🔍 Prediksi Sekarang", use_container_width=True)

    # -----------------------------------------
    # LOGIKA PREDIKSI (dijalankan setelah tombol submit)
    # -----------------------------------------
    if submitted:
        # Konversi pilihan selectbox (teks) menjadi nilai numerik sesuai encoding dataset/model
        hypertension_val = 1 if "Ya" in hypertension else 0
        diabetes_val = 1 if "Ya" in diabetes else 0
        obesity_val = 1 if "Ya" in obesity else 0
        prev_hd_val = 1 if "Ya" in prev_hd else 0

        # Pemetaan status merokok ke angka (0,1,2)
        smoking_map = {
            "Tidak Pernah (0)": 0,
            "Mantan Perokok (1)": 1,
            "Aktif Merokok (2)": 2,
        }
        # Pemetaan level aktivitas fisik ke angka (0,1,2)
        physical_map = {
            "Rendah (0)": 0,
            "Sedang (1)": 1,
            "Tinggi (2)": 2,
        }

        smoking_val = smoking_map[smoking]
        physical_val = physical_map[physical_activity]

        # Menyusun data input ke dalam DataFrame 1 baris
        # Kolom-kolomnya harus sama persis dengan fitur yang digunakan pada saat training model
        input_data = pd.DataFrame(
            [
                {
                    "age": age,
                    "hypertension": hypertension_val,
                    "blood_pressure_systolic": systolic,
                    "blood_pressure_diastolic": diastolic,
                    "diabetes": diabetes_val,
                    "cholesterol_level": cholesterol_level,
                    "cholesterol_hdl": hdl,
                    "cholesterol_ldl": ldl,
                    "triglycerides": triglycerides,
                    "fasting_blood_sugar": fasting_blood_sugar,
                    "obesity": obesity_val,
                    "waist_circumference": waist,
                    "previous_heart_disease": prev_hd_val,
                    "smoking_status": smoking_val,
                    "physical_activity": physical_val,
                }
            ]
        )

        # Mengambil model yang sudah disimpan di session_state saat training
        model = st.session_state["rf_model"]
        # Menghitung probabilitas kelas "1" (berisiko serangan jantung)
        proba = model.predict_proba(input_data)[0, 1]
        # Mengambil prediksi kelas akhir (0 = tidak berisiko, 1 = berisiko)
        pred = model.predict(input_data)[0]

        # -----------------------------------------
        # TAMPILKAN HASIL PREDIKSI
        # -----------------------------------------
        st.markdown("---")
        st.markdown("## 📊 Hasil Prediksi")

        # Dua kolom: kiri (card hasil), kanan (rekomendasi)
        col_left, col_right = st.columns([1, 1], gap="large")

        # -----------------------------
        # KARTU HASIL PROBABILITAS
        # -----------------------------
        with col_left:
            if pred == 1:
                # Jika model memprediksi BERISIKO (1)
                st.markdown(
                    f"""
                    <div style="background: linear-gradient(135deg, #dc3545 0%, #8B0000 100%); 
                               padding: 2rem; border-radius: 12px; color: white; text-align: center;">
                        <h2 style="color: white; margin-bottom: 1rem;">🚨 BERISIKO TINGGI</h2>
                        <h1 style="color: white; font-size: 3rem; margin: 0;">{proba*100:.1f}%</h1>
                        <p style="color: white; margin-top: 1rem; font-size: 1.1rem;">
                            Probabilitas Risiko Serangan Jantung
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                # Jika model memprediksi TIDAK BERISIKO (0)
                st.markdown(
                    f"""
                    <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%); 
                               padding: 2rem; border-radius: 12px; color: white; text-align: center;">
                        <h2 style="color: white; margin-bottom: 1rem;">✅ RISIKO RENDAH</h2>
                        <h1 style="color: white; font-size: 3rem; margin: 0;">{proba*100:.1f}%</h1>
                        <p style="color: white; margin-top: 1rem; font-size: 1.1rem;">
                            Probabilitas Risiko Serangan Jantung
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # -----------------------------
        # REKOMENDASI UMUM (NON-MEDIS)
        # -----------------------------
        with col_right:
            st.markdown("### 💡 Rekomendasi Umum")
            if proba >= 0.6:
                # Jika probabilitas tinggi → rekomendasi lebih serius
                st.error("⚠️ **Perhatian Serius Diperlukan**")
                st.markdown(
                    """
                    - 🏥 **Segera konsultasi** ke dokter spesialis jantung
                    - 💉 Lakukan pemeriksaan laboratorium lengkap
                    - 🚭 **Hentikan merokok** segera
                    - 🥗 Kurangi makanan tinggi lemak jenuh dan gula
                    - 🏃 Tingkatkan aktivitas fisik secara bertahap
                    - 💊 Ikuti terapi medis yang diresepkan
                    """
                )
            elif proba >= 0.3:
                # Risiko menengah → mulai perbaiki gaya hidup
                st.warning("⚠️ **Perlu Perhatian**")
                st.markdown(
                    """
                    - 👨‍⚕️ Konsultasi dengan dokter untuk pemeriksaan lanjutan
                    - 🍎 Mulai perbaiki pola makan (lebih banyak sayur dan buah)
                    - 🚶 Olahraga ringan secara teratur (minimal 30 menit/hari)
                    - 📊 Kontrol tekanan darah dan gula darah berkala
                    - 😴 Jaga pola tidur yang cukup dan teratur
                    - 🚭 Hindari merokok dan alkohol
                    """
                )
            else:
                # Risiko rendah → tetap jaga pola hidup sehat
                st.success("✅ **Kondisi Baik**")
                st.markdown(
                    """
                    - 💪 Pertahankan pola hidup sehat yang sudah ada
                    - 🏃 Tetap aktif dengan olahraga teratur
                    - 🥗 Jaga pola makan seimbang
                    - 📅 Medical check-up rutin 6-12 bulan sekali
                    - 😊 Kelola stress dengan baik
                    - 💧 Minum air putih yang cukup
                    """
                )

        # Catatan penutup sebagai disclaimer medis
        st.markdown("---")
        st.caption(
            "⚕️ **Disclaimer:** Hasil prediksi ini bersifat informatif dan tidak menggantikan diagnosis medis profesional. "
            "Selalu konsultasikan kondisi kesehatan Anda dengan dokter."
        )
