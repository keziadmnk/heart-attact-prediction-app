import streamlit as st

# Fungsi utama untuk menampilkan halaman Home
def show_home():
    # Judul utama di tengah halaman (menggunakan HTML untuk styling)
    st.markdown("<h1 style='text-align: center;'>❤️ Selamat Datang!</h1>", unsafe_allow_html=True)
    
    # Membuat layout 2 kolom: kiri lebih lebar (2 bagian) daripada kanan (1 bagian)
    col1, col2 = st.columns([2, 1], gap="large")
    
    # -----------------------------------------
    # KONTEN KIRI: Penjelasan aplikasi & alur penggunaan
    # -----------------------------------------
    with col1:
        # Card sambutan utama dengan penjelasan sistem dan langkah-langkah penggunaan
        st.markdown(
            """
            <div class="welcome-card">
                <div class="welcome-title">Sistem Prediksi Risiko Serangan Jantung di Indonesia</div>
                <div class="welcome-text">
                    Aplikasi ini membantu Anda memprediksi risiko serangan jantung berdasarkan data kesehatan 
                    dengan menggunakan Random Forest sebagai model Machine Learning.
                </div>
                <div class="welcome-text">
                    <strong>Cara Menggunakan Aplikasi:</strong>
                    <ol style="margin-top: 1rem; line-height: 2;">
                        <li><strong>Upload Dataset</strong> - Unggah file CSV data kesehatan jantung</li>
                        <li><strong>Preprocessing Data</strong> - Bersihkan dan persiapkan data untuk analisis</li>
                        <li><strong>Analisis Data</strong> - Latih model Random Forest dan lihat evaluasi performa</li>
                        <li><strong>Data Visualization</strong> - Eksplorasi visualisasi data yang informatif</li>
                        <li><strong>Prediction</strong> - Prediksi risiko serangan jantung untuk data individu</li>
                    </ol>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Tombol untuk memulai alur aplikasi
        # Saat diklik, halaman akan berpindah ke "Upload Dataset"
        if st.button("🚀 Mulai Sekarang", use_container_width=False):
            # Mengubah nilai halaman aktif di session_state
            st.session_state["page"] = "Upload Dataset"
            # Melakukan rerun app agar perubahan halaman langsung diterapkan
            st.rerun()
    
    # -----------------------------------------
    # KONTEN KANAN: Informasi singkat tentang dataset
    # -----------------------------------------
    with col2:
        # Card yang berisi ringkasan informasi dataset yang digunakan
        st.markdown(
            """
            <div class="info-card">
                <h4>📊 Info Dataset</h4>
                <ul style="list-style: none; padding: 0;">
                    <li>📁 <strong>Sumber:</strong> Kaggle</li>
                    <li>🏥 <strong>Topik:</strong> Heart Attack Prediction in Indonesia</li>
                    <li>🎯 <strong>Target:</strong> heart_attack (0 = Tidak, 1 = Ya)</li>
                    <li>📈 <strong>Fitur:</strong> 15+ variabel kesehatan</li>
                    <li>🤖 <strong>Model:</strong> Random Forest Classifier</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
