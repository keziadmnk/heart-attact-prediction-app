# state.py
import streamlit as st

def init_session_state():
    """
    Inisialisasi semua variabel st.session_state yang dibutuhkan aplikasi.

    Fungsi ini sebaiknya selalu dipanggil di awal (di app.py) agar:
    - Halaman default terset ke "Home"
    - Tempat penyimpanan dataset (raw & clean) sudah tersedia
    - Tempat penyimpanan model & daftar fitur sudah siap
    """

    # Menentukan halaman awal aplikasi (default = "Home")
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    # Menyimpan dataset mentah (hasil upload CSV) sebelum preprocessing
    if "raw_df" not in st.session_state:
        st.session_state["raw_df"] = None

    # Menyimpan dataset yang sudah melalui proses preprocessing
    if "clean_df" not in st.session_state:
        st.session_state["clean_df"] = None

    # Menyimpan model Random Forest yang sudah dilatih
    if "rf_model" not in st.session_state:
        st.session_state["rf_model"] = None

    # Menyimpan daftar nama fitur yang digunakan sebagai input model
    # Urutan dan nama kolom di sini harus sesuai dengan kolom di dataset
    if "features" not in st.session_state:
        st.session_state["features"] = [
            "age",
            "hypertension",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "diabetes",
            "cholesterol_level",
            "cholesterol_hdl",
            "cholesterol_ldl",
            "triglycerides",
            "fasting_blood_sugar",
            "obesity",
            "waist_circumference",
            "previous_heart_disease",
            "smoking_status",
            "physical_activity",
        ]


def reset_state():
    """
    OPTIONAL: Menghapus seluruh isi session_state lalu menginisialisasi ulang.

    Fungsi ini berguna jika suatu saat ingin:
    - Mengulang alur aplikasi dari awal
    - Menghapus model & data yang sudah disimpan
    Catatan: saat ini fungsi belum dipakai di UI, tapi bisa dipanggil manual jika diperlukan.
    """
    # Hapus semua key yang ada di session_state (dibuat list dulu supaya aman saat iterasi)
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Setelah kosong, set lagi ke nilai default
    init_session_state()
