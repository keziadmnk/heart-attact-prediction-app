import streamlit as st
import pandas as pd
from helpers import preprocess_data, require_raw_data  # fungsi helper untuk cek data & melakukan preprocessing


def show_preprocessing():
    # Judul utama halaman preprocessing
    st.title("Preprocessing Data")

    # Pastikan dataset mentah sudah di-upload, kalau belum akan stop dan beri peringatan
    require_raw_data()
    df_raw = st.session_state["raw_df"]  # ambil dataset mentah dari session_state

    # -----------------------------------------
    # INFORMASI AWAL DATASET
    # -----------------------------------------
    st.markdown("### 📊 Informasi Awal Dataset")
    
    # Tampilkan metrik ringkas tentang dataset asli
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        # Jumlah baris data
        st.metric("📊 Jumlah Baris", f"{df_raw.shape[0]:,}")
    with col2:
        # Jumlah kolom data
        st.metric("📋 Jumlah Kolom", f"{df_raw.shape[1]:,}")
    with col3:
        # Total nilai kosong (missing values) di seluruh kolom
        st.metric("❓ Missing Values", f"{df_raw.isna().sum().sum():,}")
    with col4:
        # Jumlah baris duplikat dalam dataset
        st.metric("🔄 Duplikat", f"{df_raw.duplicated().sum():,}")

    # Expander untuk melihat tipe data tiap kolom
    with st.expander("🔍 Lihat Tipe Data Kolom"):
        st.dataframe(
            pd.DataFrame({
                'Kolom': df_raw.dtypes.index,   # nama kolom
                'Tipe Data': df_raw.dtypes.values  # tipe data tiap kolom
            }),
            use_container_width=True
        )

    # -----------------------------------------
    # PENJELASAN PROSES PREPROCESSING
    # -----------------------------------------
    st.markdown("---")
    st.markdown("### ⚙️ Proses Preprocessing")
    st.info(
        "🔧 Preprocessing akan melakukan: penghapusan duplikat, penanganan missing values, "
        "dan konversi tipe data."
    )

    # -----------------------------
    #  TOMBOL JALANKAN PREPROCESSING
    # -----------------------------
    # Tombol untuk memulai proses preprocessing
    if st.button(" Jalankan Preprocessing", key="run_preprocess"):
        # Tampilkan spinner selama proses berjalan
        with st.spinner("⏳ Sedang memproses data..."):
            # Panggil fungsi preprocess_data dari helpers
            clean_df, info = preprocess_data(df_raw)

            # Simpan hasil preprocessing dan info ringkasan ke session_state
            st.session_state["clean_df"] = clean_df
            st.session_state["preprocess_info"] = info

        # Notifikasi sukses setelah preprocessing selesai
        st.success("✅ Preprocessing selesai!")
        # reload ulang halaman supaya blok hasil (di bawah) bisa langsung tampil
        st.rerun()

    # ----------------------------------------------------------
    #  BLOK INI SELALU JALAN JIKA clean_df SUDAH ADA DI SESSION
    # ----------------------------------------------------------
    # Jadi user tidak perlu klik preprocess ulang jika halaman direfresh
    if st.session_state.get("clean_df") is not None:

        clean_df = st.session_state["clean_df"]              # data setelah preprocessing
        info = st.session_state["preprocess_info"]           # ringkasan proses preprocessing

        st.markdown("### 📈 Ringkasan Hasil Preprocessing")

        # Tampilkan metrik hasil preprocessing (sesudah dibersihkan)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            # Jumlah baris setelah preprocessing + delta perubahan dari sebelum
            st.metric(
                "📊 Baris Setelah",
                f"{info['rows_after']:,}",
                delta=f"{info['rows_after'] - info['rows_before']:,}"
            )
        with c2:
            # Jumlah kolom aktif (fitur + target)
            st.metric("📋 Kolom Aktif", f"{info['cols']:,}")
        with c3:
            # Jumlah baris duplikat yang dihapus
            st.metric("🗑️ Duplikat Dihapus", f"{info['duplicates_removed']:,}")
        with c4:
            # Total missing values yang tersisa setelah preprocessing (harusnya 0)
            st.metric("✔️ Missing Setelah", f"{info['missing_total_after']:,}")

        # Expander untuk melihat detail jumlah missing value sebelum preprocessing
        with st.expander("📋 Detail Missing Values (Sebelum Preprocessing)"):
            missing_df = pd.DataFrame({
                'Kolom': list(info["missing_values_before"].keys()),
                'Jumlah Missing': list(info["missing_values_before"].values())
            })
            # Hanya tampilkan kolom yang benar-benar punya missing (>0)
            st.dataframe(
                missing_df[missing_df['Jumlah Missing'] > 0],
                use_container_width=True
            )

        # Preview beberapa baris pertama dari data yang sudah dibersihkan
        st.markdown("### 🔍 Preview Data Hasil Preprocessing")
        st.dataframe(clean_df.head(10), use_container_width=True)

        # Tabel statistik deskriptif (mean, std, min, max, quartile, dll.)
        st.markdown("### 📊 Statistik Deskriptif")
        st.dataframe(clean_df.describe(), use_container_width=True)

        # -----------------------------
        #     TOMBOL NAVIGASI
        # -----------------------------
        # Tombol Previous di ujung kiri dan Next di ujung kanan, sejajar dengan konten
        col_prev, col_spacer, col_next = st.columns([3, 6, 3], gap="large")
        
        with col_prev:
            
            # Tombol Previous untuk kembali ke halaman Upload Dataset
            if st.button("< Previous", key="goto_upload", use_container_width=False):
                st.session_state["page"] = "Upload Dataset"
                st.rerun()
        
        with col_spacer:
            # Spacer kosong
            st.empty()
        
        with col_next:
            # Tombol Next untuk berpindah ke halaman Analisis Data (training model)
            if st.button("Next >", key="goto_training", use_container_width=False):
                st.session_state["page"] = "Analisis Data"  # ubah target halaman di session_state
                st.rerun()  # reload app agar router di app.py mengarahkan ke halaman analisis
        
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

        # Info bahwa data preprocessing sudah siap dipakai di tahap berikutnya
        st.info("✅ Data preprocessing sudah tersimpan dan siap untuk dianalisis.")
