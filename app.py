import streamlit as st

# load external modules
from style import add_custom_css      
from state import init_session_state  
from helpers import TARGET_COL        

# import pages
from pages.home import show_home                      
from pages.upload_dataset import show_upload_dataset  
from pages.preprocessing import show_preprocessing    
from pages.analysis import show_analysis              
from pages.visualization import show_visualization    
from pages.prediction import show_prediction          
from pages.about import show_about                    


# ----------------------------
#   STREAMLIT CONFIG
# ----------------------------
st.set_page_config(
    page_title="Prediksi Risiko Serangan Jantung",
    layout="wide"
)


# ----------------------------
#   INIT SESSION STATE
# ----------------------------
init_session_state()


# ----------------------------
#   LOAD GLOBAL CSS
# ----------------------------
add_custom_css()


# ----------------------------
#   SIDEBAR NAVIGATION
# ----------------------------
with st.sidebar:
    # Logo di bagian atas sidebar
    import os
    from pathlib import Path
    
    logo_path = os.path.join(Path(__file__).parent, 'static/logo1.png')
    
    if os.path.exists(logo_path):
        from PIL import Image
        logo = Image.open(logo_path)
        st.image(logo, use_container_width=True)
    else:
        st.markdown("""
        <div class="logo-container">
            <div class="logo-text">LOGO</div>
        </div>
        """, unsafe_allow_html=True)
        st.warning("Logo tidak ditemukan. Pastikan file logo1.png ada di folder static/")

    # Menu items
    menu_items = [
        "Home",
        "Upload Dataset",
        "Preprocessing Data",
        "Analisis Data",
        "Data Visualization",
        "Prediction",
        "About"
    ]
    
    # Render custom menu
    st.markdown('<div class="custom-menu">', unsafe_allow_html=True)
    for item in menu_items:
        # Cek apakah ini menu yang aktif
        is_active = st.session_state["page"] == item
        active_class = "active" if is_active else ""
        
        # Buat unique key untuk setiap button
        button_key = f"menu_{item.replace(' ', '_').lower()}"
        
        # Render menu item sebagai button dengan styling khusus
        if st.button(
            item,
            key=button_key,
            use_container_width=True,
            type="secondary" if not is_active else "primary"
        ):
            st.session_state["page"] = item
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)


# ----------------------------
#   PAGE ROUTER
# ----------------------------
if st.session_state["page"] == "Home":
    show_home()

elif st.session_state["page"] == "Upload Dataset":
    show_upload_dataset()

elif st.session_state["page"] == "Preprocessing Data":
    show_preprocessing()

elif st.session_state["page"] == "Analisis Data":
    show_analysis()

elif st.session_state["page"] == "Data Visualization":
    show_visualization()

elif st.session_state["page"] == "Prediction":
    show_prediction()

elif st.session_state["page"] == "About":
    show_about()