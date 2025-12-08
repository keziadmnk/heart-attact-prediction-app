# pages/about.py
import streamlit as st


def show_about():
    st.title("ℹ Tentang Aplikasi")

    # Card Header
    st.markdown(
        """
        <div class="welcome-card">
            <h3>📱 Sistem Prediksi Risiko Serangan Jantung di Indonesia</h3>
            <p style="line-height: 1.8; color: #555;">
                Aplikasi ini dikembangkan sebagai tugas besar mata kuliah <strong>Akuisisi Data</strong> 
                di Program Studi Sistem Informasi, Fakultas Teknologi Informasi, Universitas Andalas.
            </p>
            <p style="line-height: 1.8; color: #555;">
                Menggunakan algoritma <strong>Random Forest Classifier</strong> untuk memprediksi 
                probabilitas risiko serangan jantung berdasarkan data kesehatan dan gaya hidup pasien.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    # ==========================
    # KOLOM KIRI — TIM & DOSEN
    # ==========================
    with col1:
        st.markdown("### 👥 Kelompok 4 - Tim Pengembang")

        # Data anggota tim + FOTO YANG BENAR
        team_members = [
            ("Nayla Thahira Meldian", "2311521006", "static/nayla.jpg"),
            ("Kezia Valerina Damanik", "2311522010", "static/kezia.jpg"),
            ("Aisyah Insani Aulia", "2311523024", "static/aisyah.jpeg"),
        ]

        # Render card untuk tiap anggota (pakai st.image agar foto pasti tampil)
        for name, nim, img_path in team_members:
            with st.container():
                colA, colB = st.columns([1, 3])

                with colA:
                    st.image(img_path, width=90)

                with colB:
                    st.markdown(f"**{name}**")
                    st.markdown(
                        f"<span style='color:#777;'>NIM: {nim}</span>",
                        unsafe_allow_html=True,
                    )

        # Dosen Pengampu
        st.markdown("### 👨‍🏫 Dosen Pengampu")
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
    # KOLOM KANAN — TEKNOLOGI
    # ==========================
    with col2:
        st.markdown("### 🛠️ Teknologi yang Digunakan")
        st.markdown(
            """
            <div class="data-card">
                <ul style="line-height: 2;">
                    <li>🐍 <strong>Python</strong></li>
                    <li>🎨 <strong>Streamlit</strong></li>
                    <li>📊 <strong>Pandas & NumPy</strong></li>
                    <li>🤖 <strong>Scikit-learn</strong></li>
                    <li>📈 <strong>Matplotlib & Seaborn</strong></li>
                    <li>🌳 <strong>Random Forest</strong></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ======================
    # ALUR APLIKASI
    # ======================
    st.markdown("### 🔄 Alur Kerja Aplikasi")

    steps = [
        ("1️⃣", "Home", "Pengenalan aplikasi dan tombol mulai"),
        ("2️⃣", "Upload Dataset", "Unggah file CSV dataset kesehatan jantung"),
        ("3️⃣", "Preprocessing Data", "Membersihkan data dan menangani missing values"),
        ("4️⃣", "Analisis Data", "Training model Random Forest dan evaluasi performa"),
        ("5️⃣", "Data Visualization", "Eksplorasi grafik distribusi, korelasi, dan feature importance"),
        ("6️⃣", "Prediction", "Input data & prediksi risiko"),
        ("7️⃣", "About", "Informasi tim dan teknologi"),
    ]

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

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #8B0000 0%, #c62828 100%); 
                    border-radius: 4px; color: white;">
            <h3>Terima kasih telah menggunakan aplikasi ini!</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
