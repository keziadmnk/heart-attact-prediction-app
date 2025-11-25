# pages/about.py
import streamlit as st


def show_about():
    # Judul utama halaman "About"
    st.title("ℹ️ Tentang Aplikasi")

    # Card deskripsi umum aplikasi (dibuat dengan HTML + CSS custom dari style.py)
    st.markdown(
        """
        <div class="welcome-card">
            <h3>📱 Sistem Prediksi Risiko Serangan Jantung di Indonesia</h3>
            <p style="line-height: 1.8; color: #555;">
                Aplikasi ini dikembangkan sebagai tugas besar mata kuliah <strong>Akuisisi Data</strong> 
                di Program Studi Sistem Informasi, Fakultas Teknologi Informasi, Universitas Andalas.
            </p>
            <p style="line-height: 1.8; color: #555;">
                Memanfaatkan algoritma <strong>Random Forest Classifier</strong> untuk memprediksi 
                probabilitas risiko serangan jantung berdasarkan data kesehatan dan gaya hidup pasien.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Membuat layout 2 kolom: kiri (tim & dosen), kanan (teknologi)
    col1, col2 = st.columns(2, gap="large")

    # =======================
    # KOLOM KIRI: TIM & DOSEN
    # =======================
    with col1:
        # Subjudul bagian tim pengembang
        st.markdown("### 👥 Kelompok 4 - Tim Pengembang")
        # Card berisi daftar anggota kelompok
        st.markdown(
            """
            <div class="data-card">
                <ul style="list-style: none; padding: 0; line-height: 2.5;">
                    <li>👤 <strong>Nayla Thahira Meldian</strong> — 2311521006</li>
                    <li>👤 <strong>Kezia Valerina Damanik</strong> — 2311522010</li>
                    <li>👤 <strong>Aisyah Insani Aulia</strong> — 2311523024</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Subjudul dosen pengampu
        st.markdown("### 👨‍🏫 Dosen Pengampu")
        # Card nama dosen pengampu
        st.markdown(
            """
            <div class="data-card">
                <p style="font-size: 1.1rem; color: #555;">
                    <strong>Rahmatika Pratama Santi, M.T</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ==========================
    # KOLOM KANAN: TEKNOLOGI
    # ==========================
    with col2:
        # Subjudul teknologi yang digunakan dalam proyek
        st.markdown("### 🛠️ Teknologi yang Digunakan")
        # Card daftar tools / library yang dipakai
        st.markdown(
            """
            <div class="data-card">
                <ul style="line-height: 2;">
                    <li>🐍 <strong>Python</strong> - Bahasa pemrograman</li>
                    <li>🎨 <strong>Streamlit</strong> - Framework web interaktif</li>
                    <li>📊 <strong>Pandas & NumPy</strong> - Pengolahan data</li>
                    <li>🤖 <strong>Scikit-learn</strong> - Machine learning</li>
                    <li>📈 <strong>Matplotlib & Seaborn</strong> - Visualisasi</li>
                    <li>🌳 <strong>Random Forest</strong> - Algoritma prediksi</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Judul bagian alur kerja aplikasi
    st.markdown("### 🔄 Alur Kerja Aplikasi")

    # List berisi tahapan alur kerja, tiap item = (ikon, judul bagian, deskripsi singkat)
    steps = [
        ("1️⃣", "Home", "Pengenalan aplikasi dan tombol mulai"),
        ("2️⃣", "Upload Dataset", "Unggah file CSV dataset kesehatan jantung"),
        ("3️⃣", "Preprocessing Data", "Pembersihan data dan penanganan missing values"),
        ("4️⃣", "Analisis Data", "Training model Random Forest dan evaluasi performa"),
        ("5️⃣", "Data Visualization", "Eksplorasi grafik distribusi, korelasi, dan feature importance"),
        ("6️⃣", "Prediction", "Input data kesehatan personal dan prediksi risiko"),
        ("7️⃣", "About", "Informasi tim pengembang dan teknologi"),
    ]

    # Loop untuk menampilkan setiap step sebagai kartu (card) terpisah
    for icon, title, desc in steps:
        st.markdown(
            f"""
            <div class="data-card" style="margin-bottom: 1rem;">
                <h4 style="color: #8B0000; margin-bottom: 0.5rem;">{icon} {title}</h4>
                <p style="color: #666; margin: 0;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Garis pemisah sebelum footer terima kasih
    st.markdown("---")
    # Footer ucapan terima kasih di bagian bawah halaman About
    st.markdown(
        """
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #8B0000 0%, #c62828 100%); 
                    border-radius: 12px; color: white;">
            <h3 style="color: white;">❤️ Terima kasih telah menggunakan aplikasi ini!</h3>
            <p style="color: white; margin-top: 1rem;">
                Dikembangkan dengan ❤️ oleh Kelompok 4 - Sistem Informasi UNAND
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
