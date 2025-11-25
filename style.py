import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.

    Fungsi ini dipanggil sekali di app.py agar:
    - Tampilan aplikasi lebih konsisten (font, warna, layout)
    - Sidebar, tombol, card, dan komponen lain punya style yang seragam
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts: menggunakan font Inter untuk seluruh aplikasi */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Global Styles: semua elemen memakai font Inter */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Area utama konten (body) Streamlit */
        .main {
            background-color: #f8f9fa;
            padding: 2rem;
        }
        
        /* Styling untuk sidebar (background merah gradasi) */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #8B0000 0%, #6B0000 100%);
            padding-top: 2rem;
        }
        
        /* Semua elemen di dalam sidebar diberi warna teks putih */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Container untuk logo di sidebar */
        .logo-container {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 2rem;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Teks logo di sidebar */
        .logo-text {
            font-size: 1.2rem;
            font-weight: 700;
            color: white;
            letter-spacing: 2px;
        }
        
        /* Label radio button di sidebar (judul menu) */
        .stRadio > label {
            font-size: 0.9rem;
            font-weight: 500;
            color: white !important;
        }
        
        /* Jarak antar opsi radio di sidebar */
        [data-testid="stSidebar"] .stRadio > div {
            gap: 0.5rem;
        }
        
        /* Style untuk setiap label opsi radio (seperti card kecil) */
        [data-testid="stSidebar"] .stRadio label {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        /* Efek hover pada label radio (sedikit terang + geser ke kanan) */
        [data-testid="stSidebar"] .stRadio label:hover {
            background-color: rgba(255, 255, 255, 0.2);
            transform: translateX(5px);
        }
        
        /* Card sambutan di halaman Home (putih dengan bayangan) */
        .welcome-card {
            background: white;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-left: 5px solid #8B0000;
            margin-bottom: 2rem;
        }
        
        /* Judul besar di welcome card */
        .welcome-title {
            font-size: 2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        /* Paragraf di welcome card */
        .welcome-text {
            font-size: 1rem;
            color: #555;
            line-height: 1.8;
            margin-bottom: 1.5rem;
        }
        
        /* Card informasi dataset di Home (merah gradasi) */
        .info-card {
            background: linear-gradient(135deg, #8B0000 0%, #c62828 100%);
            color: white;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(139,0,0,0.3);
            height: 100%;
        }
        
        /* Judul dalam info-card */
        .info-card h4 {
            color: white !important;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        /* List di dalam info-card dihilangkan bullet-nya */
        .info-card ul {
            list-style: none;
            padding: 0;
        }
        
        /* Setiap item list di info-card diberi border bawah tipis */
        .info-card li {
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }
        
        /* Item terakhir list tanpa border bawah */
        .info-card li:last-child {
            border-bottom: none;
        }
        
        /* Styling umum untuk semua tombol Streamlit */
        .stButton > button {
            background: linear-gradient(135deg, #c62828 0%, #8B0000 100%);
            color: white;
            border-radius: 10px;
            padding: 0.75rem 2rem;
            border: none;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(198,40,40,0.3);
            width: auto;
        }
        
        /* Efek hover tombol (warna gradasi dibalik + sedikit naik) */
        .stButton > button:hover {
            background: linear-gradient(135deg, #8B0000 0%, #c62828 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(198,40,40,0.4);
        }
        
        /* Angka utama di komponen st.metric (nilai besar) */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #8B0000;
        }
        
        /* Label kecil di bawah/atas nilai metric */
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            color: #666;
            font-weight: 500;
        }
        
        /* Card data umum (dipakai di banyak halaman) */
        .data-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            margin-bottom: 1.5rem;
            border: 1px solid #eee;
        }
        
        /* Style umum untuk heading h1 (judul besar halaman) */
        h1 {
            color: #2c3e50;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        
        /* Style untuk heading h2 dan h3 (subjudul) */
        h2, h3 {
            color: #34495e;
            font-weight: 600;
        }
        
        /* Area upload file (st.file_uploader) diberi border dashed */
        [data-testid="stFileUploader"] {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            border: 2px dashed #8B0000;
        }
        
        /* Tabs container: beri jarak antar tab */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
        }
        
        /* Style setiap tab (seperti pill putih dengan border) */
        .stTabs [data-baseweb="tab"] {
            background-color: white;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            border: 2px solid #eee;
            font-weight: 600;
        }
        
        /* Tab yang aktif diberi background merah dan teks putih */
        .stTabs [aria-selected="true"] {
            background-color: #8B0000;
            color: white;
            border-color: #8B0000;
        }
        
        /* Form (st.form) dibuat seperti card putih dengan bayangan */
        .stForm {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        }
        
        /* Style untuk pesan success (st.success) */
        .stSuccess {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
            border-radius: 8px;
        }
        
        /* Style untuk pesan error (st.error) */
        .stError {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            border-radius: 8px;
        }
        
        /* Style untuk pesan warning (st.warning) */
        .stWarning {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            border-radius: 8px;
        }
        
        /* Style untuk pesan info (st.info) */
        .stInfo {
            background-color: #d1ecf1;
            border-left: 4px solid #17a2b8;
            border-radius: 8px;
        }
        
        /* Header expander (komponen collapsible) dibuat seperti card putih */
        .streamlit-expanderHeader {
            background-color: white;
            border-radius: 8px;
            font-weight: 600;
        }
        
        /* DataFrame (tabel) dibuat dengan sudut membulat dan overflow tersembunyi */
        [data-testid="stDataFrame"] {
            border-radius: 8px;
            overflow: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
