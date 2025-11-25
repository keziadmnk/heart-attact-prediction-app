import streamlit as st

# load external modules
from style import add_custom_css      # fungsi untuk memuat CSS khusus (style tampilan) dari file style.py
from state import init_session_state  # fungsi untuk inisialisasi semua variabel di st.session_state dari file state.py
from helpers import TARGET_COL        # konstanta nama kolom target (misal: 'heart_attack')

# import pages
from pages.home import show_home                      # fungsi untuk menampilkan halaman Home
from pages.upload_dataset import show_upload_dataset  # fungsi untuk menampilkan halaman Upload Dataset
from pages.preprocessing import show_preprocessing    # fungsi untuk menampilkan halaman Preprocessing Data
from pages.analysis import show_analysis              # fungsi untuk menampilkan halaman Analisis / Training Model
from pages.visualization import show_visualization    # fungsi untuk menampilkan halaman Visualisasi Data
from pages.prediction import show_prediction          # fungsi untuk menampilkan halaman Prediksi
from pages.about import show_about                    # fungsi untuk menampilkan halaman Tentang Aplikasi


# ----------------------------
#   STREAMLIT CONFIG
# ----------------------------
st.set_page_config(
    page_title="Prediksi Risiko Serangan Jantung",  # judul tab browser
    layout="wide"                                   # layout lebar (full width)
)


# ----------------------------
#   INIT SESSION STATE
# ----------------------------
# Pastikan semua key penting di st.session_state sudah ada (page, raw_df, clean_df, rf_model, dll.)
# Agar tidak error saat diakses di halaman lain.
init_session_state()


# ----------------------------
#   LOAD GLOBAL CSS
# ----------------------------
# Memasukkan CSS kustom ke dalam aplikasi supaya tampilan lebih cantik (sidebar merah, card, dll.)
add_custom_css()


# ----------------------------
#   SIDEBAR NAVIGATION
# ----------------------------
with st.sidebar:
    # Logo di bagian atas sidebar (pakai HTML + CSS yang sudah didefinisikan di style.py)
    st.markdown("""
    <div class="logo-container">
        <div class="logo-text">LOGO</div>
    </div>
    """, unsafe_allow_html=True)

    # Radio button untuk navigasi antar halaman
    # value default diambil dari st.session_state["page"],
    # jadi kalau kita ubah page lewat kode (misal di tombol "Lanjut"), radio ini ikut berpindah.
    menu = st.radio(
        "Navigasi",
        (
            "Home",
            "Upload Dataset",
            "Preprocessing Data",
            "Analisis Data",
            "Data Visualization",
            "Prediction",
            "About"
        ),
        index=[
            "Home",
            "Upload Dataset",
            "Preprocessing Data",
            "Analisis Data",
            "Data Visualization",
            "Prediction",
            "About",
        ].index(st.session_state["page"]),  # menentukan posisi awal radio sesuai page yang tersimpan
    )

# Simpan pilihan menu user ke session_state["page"]
# sehingga bisa dipakai di router di bawah.
st.session_state["page"] = menu


# ----------------------------
#   PAGE ROUTER
# ----------------------------
# Bagian ini seperti "switch-case": tergantung nilai st.session_state["page"],
# kita panggil fungsi halaman yang sesuai.
if st.session_state["page"] == "Home":
    # Tampilkan halaman Home
    show_home()

elif st.session_state["page"] == "Upload Dataset":
    # Tampilkan halaman upload dataset
    show_upload_dataset()

elif st.session_state["page"] == "Preprocessing Data":
    # Tampilkan halaman preprocessing data
    show_preprocessing()

elif st.session_state["page"] == "Analisis Data":
    # Tampilkan halaman analisis dan training model
    show_analysis()

elif st.session_state["page"] == "Data Visualization":
    # Tampilkan halaman visualisasi data
    show_visualization()

elif st.session_state["page"] == "Prediction":
    # Tampilkan halaman prediksi risiko serangan jantung
    show_prediction()

elif st.session_state["page"] == "About":
    # Tampilkan halaman tentang aplikasi dan tim pengembang
    show_about()
