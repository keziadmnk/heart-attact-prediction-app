import streamlit as st
import pandas as pd

# Fungsi utama halaman "Upload Dataset"
def show_upload_dataset():
    # Judul halaman
    st.title("📂 Upload Dataset")
    
    # Card penjelasan singkat tentang apa yang harus dilakukan user di halaman ini
    st.markdown(
        """
        <div class="data-card">
            <p style="font-size: 1 rem; color: #555; margin-bottom: 1rem;">
                Silakan unggah file <strong>CSV</strong> dataset <em>Heart Attack Prediction in Indonesia</em> dari Kaggle.
                Setelah upload berhasil, preview data akan ditampilkan.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Komponen untuk memilih & mengunggah file CSV
    uploaded_file = st.file_uploader(
        "Pilih file CSV",
        type=["csv"],
        help="Upload file CSV dengan format yang sesuai"
    )

    # Jika user sudah memilih file
    if uploaded_file is not None:
        try:
            # Baca file CSV menjadi DataFrame pandas
            df = pd.read_csv(uploaded_file)

            # Simpan dataset mentah ke session_state supaya bisa dipakai di halaman lain
            st.session_state["raw_df"] = df

            # Notifikasi bahwa upload berhasil
            st.success("✅ Dataset berhasil diupload!")
            
            # -----------------------------
            #  METRIK RINGKAS DATASET
            # -----------------------------
            col1, col2, col3 = st.columns(3)
            with col1:
                # Total baris data
                st.metric("📊 Total Baris", f"{df.shape[0]:,}")
            with col2:
                # Total kolom data
                st.metric("📋 Total Kolom", f"{df.shape[1]:,}")
            with col3:
                # Perkiraan ukuran memori DataFrame (dalam KB)
                st.metric(
                    "💾 Ukuran Data",
                    f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB"
                )

            # Tampilkan 5 baris pertama sebagai preview
            st.markdown("### 🔍 Preview Data (5 baris pertama)")
            st.dataframe(df.head(), use_container_width=True)
            
            # -----------------------------
            #  INFORMASI TIPE & MISSING
            # -----------------------------
            st.markdown("### 📈 Informasi Kolom")
            col_info = pd.DataFrame({
                'Kolom': df.columns,              # nama kolom
                'Tipe Data': df.dtypes.values,    # tipe data per kolom
                'Non-Null Count': df.count().values,   # jumlah data tidak null
                'Null Count': df.isna().sum().values   # jumlah data null per kolom
            })
            st.dataframe(col_info, use_container_width=True)

            # Tombol untuk langsung pindah ke halaman preprocessing
            if st.button("➡️ Lanjut ke Preprocessing", use_container_width=False):
                st.session_state["page"] = "Preprocessing Data"  # update halaman aktif
                st.rerun()  # refresh app agar router di app.py mengarahkan ke halaman berikutnya
                
        except Exception as e:
            # Jika gagal membaca CSV, tampilkan pesan error
            st.error(f"❌ Terjadi kesalahan saat membaca file CSV: {e}")
            st.info("💡 Pastikan file CSV Anda memiliki format yang benar dan tidak corrupt.")
