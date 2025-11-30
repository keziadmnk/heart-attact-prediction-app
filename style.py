import streamlit as st

def add_custom_css():
    """
    Menyuntikkan (inject) CSS kustom ke dalam aplikasi Streamlit.
    """
    st.markdown(
        """
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Area utama konten */
        .main {
            background-color: #f8f9fa;
            padding: 0rem;
        }
        
        /* Styling untuk sidebar - warna solid tanpa gradasi */
        [data-testid="stSidebar"] {
            background: #7C1F1D;
            padding-top: 0rem;
        }
        
        /* Semua elemen di dalam sidebar */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Container untuk logo */
        .logo-container {
            background-color: transparent;
            padding: 2rem;
            border: none;
            shadow: none;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        /* Sembunyikan navigation bar default */
        [data-testid="stSidebarNav"] {
            display: none;
        }

        /* Hapus margin atas pada elemen pertama di sidebar */
        [data-testid="stSidebar"] > div:first-child {
            margin-top: 0 !important;
        }
        
        /* Custom Menu Container */
        .custom-menu {
            display: flex;
            flex-direction: column;
            gap: 0rem;
            padding: 0rem 1rem;
        }
        
        /* Styling untuk semua button menu di sidebar */
        [data-testid="stSidebar"] .stButton > button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.75rem 1rem !important;
            font-weight: 500 !important;
            font-size: 1rem !important;
            text-align: left !important;
            justify-content: flex-start !important;
            width: 100% !important;
            transition: all 0.2s ease !important;
            box-shadow: none !important;
            margin: 0 !important;
            border-left: 4px solid transparent !important;
        }
        
        /* Hover state untuk menu - sedikit lebih gelap */
        [data-testid="stSidebar"] .stButton > button:hover {
            background-color: rgba(0, 0, 0, 0.15) !important;
            border-left: 4px solid rgba(255, 255, 255, 0.3) !important;
        }
        
        /* Active state untuk menu - border putih di kiri */
        [data-testid="stSidebar"] button[kind="primary"] {
            background-color: rgba(0, 0, 0, 0.2) !important;
            font-weight: 600 !important;
            border-left: 4px solid white !important;
        }
        
        /* Active state hover */
        [data-testid="stSidebar"] button[kind="primary"]:hover {
            background-color: rgba(0, 0, 0, 0.25) !important;
        }
        
        /* Card sambutan di halaman Home */
        .welcome-card {
            background: white;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-left: 5px solid #7C1F1D;
            margin-bottom: 2rem;
        }
        
        .welcome-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        .welcome-text {
            font-size: 0.9rem;
            color: #555;
            line-height: 1.8;
            margin-bottom: 1rem;
        }
        
        /* Card informasi dataset */
        .info-card {
            background: #A62D2B;
            color: white;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(124,31,29,0.3);
            height: 100%;
        }
        
        .info-card h4 {
            color: white !important;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        .info-card ul {
            list-style: none;
            padding: 0;
        }
        
        .info-card li {
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }
        
        .info-card li:last-child {
            border-bottom: none;
        }
        
        /* Styling umum untuk tombol */
        .stButton > button {
            background: #A62D2B;
            color: white;
            border-radius: 10px;
            padding: 0.75rem 2rem;
            border: none;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(124,31,29,0.3);
            width: auto;
        }
        
        .stButton > button:hover {
            background: #5d1715;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(124,31,29,0.4);
        }
        
        /* Tombol Previous (abu-abu) */
        .nav-button-prev {
            background: #6c757d !important;
            color: white !important;
            border: none !important;
            border-radius: 10px;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(108, 117, 125, 0.3);
            white-space: nowrap !important;
            text-align: center !important;
            display: inline-block !important;
            width: auto !important;
            min-width: 120px !important;
        }
        
        .nav-button-prev:hover {
            background: #5a6268 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(108, 117, 125, 0.4);
        }
        
        /* Tombol Next (merah) */
        .nav-button-next {
            background: #7C1F1D !important;
            color: white !important;
            border: none !important;
            border-radius: 10px;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(124,31,29,0.3);
            white-space: nowrap !important;
            text-align: center !important;
            display: inline-block !important;
            width: auto !important;
            min-width: 120px !important;
        }
        
        .nav-button-next:hover {
            background: #5d1715 !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(124,31,29,0.4);
        }
        
        /* Container alignment untuk button navigasi */
        div[data-testid="column"]:last-of-type {
            display: flex !important;
            justify-content: flex-end !important;
            align-items: center;
            width: 100%;
        }
        
        div[data-testid="column"]:last-of-type .stButton {
            width: auto !important;
            margin-left: auto !important;
        }
        
        div[data-testid="column"]:last-of-type .stButton > button {
            width: auto !important;
            min-width: 120px;
            margin-left: auto !important;
        }
        
        div[data-testid="column"]:first-of-type {
            display: flex !important;
            justify-content: flex-start !important;
            align-items: center;
            width: 100%;
        }
        
        div[data-testid="column"]:first-of-type .stButton {
            width: auto !important;
            margin-right: auto !important;
        }
        
        div[data-testid="column"]:first-of-type .stButton > button {
            width: auto !important;
            min-width: 120px;
            margin-right: auto !important;
        }
        
        /* Metric styling */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #7C1F1D;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            color: #666;
            font-weight: 500;
        }
        
        /* Data card */
        .data-card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            margin-bottom: 1.5rem;
            border: 1px solid #eee;
        }
        
        /* Headings */
        h1 {
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
        }
        
        h2, h3 {
            color: #34495e;
            font-weight: 600;
        }
        
        /* File uploader */
        [data-testid="stFileUploader"] {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            border: 2px dashed #7C1F1D;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: white;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            border: 2px solid #eee;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background-color: #f5f5f5;
            border-color: #7C1F1D;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #7C1F1D;
            color: white;
            border-color: #7C1F1D;
            box-shadow: 0 4px 12px rgba(124, 31, 29, 0.3);
        }

        .stTabs [aria-selected="true"]:hover {
            background-color: #5d1715;
            border-color: #5d1715;
            box-shadow: 0 6px 16px rgba(124, 31, 29, 0.4);
        }
        
        /* Form styling */
        .stForm {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        }
        
        /* Alert messages */
        .stSuccess {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
            border-radius: 8px;
        }
        
        .stError {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            border-radius: 8px;
        }
        
        .stWarning {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            border-radius: 8px;
        }
        
        .stInfo {
            background-color: #d1ecf1;
            border-left: 4px solid #17a2b8;
            border-radius: 8px;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background-color: white;
            border-radius: 8px;
            font-weight: 600;
        }
        
        /* DataFrame */
        [data-testid="stDataFrame"] {
            border-radius: 8px;
            overflow: hidden;
        }

        /* Image and chart borders */
        [data-testid="stImage"],
        .stPlotlyChart,
        .streamlit-expanderContent > div > div:first-child > div:nth-child(2) {
            border: 1px solid #7C1F1D; 
            border-radius: 8px; 
            padding: 15px; 
            background-color: transparent; 
            margin-bottom: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )