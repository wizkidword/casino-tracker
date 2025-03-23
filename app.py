import streamlit as st
import json
import os

# SEO-friendly title (must be the first Streamlit command)
st.set_page_config(
    page_title="Best Free Social Casinos & Bonuses for 2025",
    page_icon="🎰",
    layout="wide"
)

# Add casino-themed background with overlay, text color adjustments, and thematic font
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');
    div[data-testid="stApp"] {
        background-image: url('https://cdn.pixabay.com/photo/2013/12/12/22/11/game-casino-227586_1280.jpg') !important;
        background-size: cover !important;
        background-attachment: fixed !important;
        background-position: center !important;
        background-color: #1a1a1a !important; /* Fallback color */
    }
    /* Add a semi-transparent overlay to improve text readability */
    div[data-testid="stApp"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.6); /* Dark overlay with 60% opacity */
        z-index: -1;
    }
    /* Adjust text colors for better contrast */
    h1, h2, h3, p, div, span, a {
        color: #f0f0f0 !important; /* Light gray/white text for readability */
    }
    /* Use a thematic font for headers */
    h1, h2, h3 {
        font-family: 'Luckiest Guy', cursive !important;
        color: gold !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    /* Style the sidebar with a dark background */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #1a1a1a, #333333);
    }
    /* Ensure sidebar text is readable */
    [data-testid="stSidebar"] * {
        color: gold !important;
    }
    /* Style for the casino container */
    .casino-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }
    /* Style for the logo container */
    .logo-button-container {
        position: relative;
        width: 125px;
        height: 125px;
        cursor: pointer;
    }
    /* Target the Streamlit image container */
    div[data-testid="stImage"] {
        width: 125px !important;
        height: 125px !important;
        transition: all 0.3s ease;
        border: 2px solid gold;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 5px;
        box-sizing: border-box;
    }
    div[data-testid="stImage"] img {
        width: 100% !important;
        height: 100% !important;
        object-fit: contain;
        border-radius: 8px;
    }
    div[data-testid="stImage"]:hover {
        opacity: 1;
        box-shadow: 0 0 15px gold, 0 0 30px rgba(255, 215, 0, 0.5);
    }
    /* Style for the text button container */
    .text-button-container {
        z-index: 2;
    }
    /* Style for the text buttons below logos */
    .casino-button {
        display: inline-block;
        width: 125px;
        text-align: center;
        padding: 5px 0;
        background-color: rgba(0, 0, 0, 0.8);
        color: gold !important;
        font-size: 14px;
        font-weight: bold;
        border: 1px solid gold;
        border-radius: 5px;
        transition: all 0.3s ease;
        cursor: pointer;
        margin-top: 10px;
    }
    .casino-button:hover {
        background-color: rgba(255, 215, 0, 0.2);
        box-shadow: 0 0 10px gold;
        color: white !important;
    }
    /* Style the Streamlit button to overlay the image */
    div[data-testid="stButton"] button {
        position: absolute;
        top: 0;
        left: 0;
        width: 125px;
        height: 125px;
        opacity: 0; /* Make the button invisible but clickable */
        z-index: 2; /* Ensure the button is above the image */
        cursor: pointer;
        border: none;
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# File paths
CASINO_FILE = 'casinos.json'
DATA_FILE = 'casino_data.json'

# Load casino data with error handling
def load_casinos():
    try:
        if os.path.exists(CASINO_FILE):
            with open(CASINO_FILE, 'r') as f:
                return json.load(f)
        return {
            "Slotomania": "https://www.slotomania.com/?ref=your_ref_link",
            "DoubleDown Casino": "https://www.doubledowncasino.com/?ref=your_ref_link",
        }
    except Exception as e:
        st.error(f"Error loading casinos.json: {e}")
        return {
            "Slotomania": "https://www.slotomania.com/?ref=your_ref_link",
            "DoubleDown Casino": "https://www.doubledowncasino.com/?ref=your_ref_link",
        }

def load_casino_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {}
    except Exception as e:
        st.error(f"Error loading casino_data.json: {e}")
        return {}

casinos = load_casinos()
casino_data = load_casino_data()

# Main content
st.title("Best Free Social Casinos & Bonuses for 2025")

# Add a hidden input to capture the selected casino
if 'selected_casino' not in st.session_state:
    st.session_state.selected_casino = None

# Sidebar with centered title
with st.sidebar:
    if st.session_state.get('selected_casino') and st.session_state.selected_casino in casinos:
        st.markdown(
            f"<h2 style='text-align: center;'>{st.session_state.selected_casino}</h2>",
            unsafe_allow_html=True
        )
        st.write(f"**Signup:** [Get Your Bonus Here]({casinos[st.session_state.selected_casino]})")
        st.write(f"**Free Daily SC:** {casino_data.get(st.session_state.selected_casino, {}).get('free_daily_sc', 'N/A')}")
        st.write(f"**Daily Amount:** {casino_data.get(st.session_state.selected_casino, {}).get('daily_amount', 'N/A')}")
        st.write(f"**Min. Cash Redeem:** {casino_data.get(st.session_state.selected_casino, {}).get('min_cash_redeem', 'N/A')}")
        st.write(f"**Gift Cards:** {casino_data.get(st.session_state.selected_casino, {}).get('gift_cards', 'N/A')}")
        st.write(f"**Crypto:** {casino_data.get(st.session_state.selected_casino, {}).get('crypto', 'N/A')}")
        st.write(f"**VIP System:** {casino_data.get(st.session_state.selected_casino, {}).get('vip_system', 'N/A')}")
        st.write(f"**Farm VIP w/GC:** {casino_data.get(st.session_state.selected_casino, {}).get('farm_vip_with_gc', 'N/A')}")
        st.write(f"**Notes:** {casino_data.get(st.session_state.selected_casino, {}).get('notes', 'No notes available.')}")
    else:
        st.write("Select a casino to view details.")

# Casino grid
if casinos:
    cols = st.columns(6)
    for i, (name, url) in enumerate(casinos.items()):
        col_idx = i % 6
        with cols[col_idx]:
            # Wrap the logo and button in a container for better spacing
            st.markdown('<div class="casino-container">', unsafe_allow_html=True)
            
            logo_path = f"static/{name.lower().replace(' ', '_')}.png"
            placeholder_path = "static/placeholder.png"
            
            # Wrap the image and button in a container
            st.markdown(f'<div class="logo-button-container">', unsafe_allow_html=True)
            
            # Load image using st.image
            try:
                if os.path.exists(logo_path):
                    st.image(logo_path, width=125)
                else:
                    st.write(f"Logo not found: {logo_path}")
                    if os.path.exists(placeholder_path):
                        st.image(placeholder_path, width=125, caption="Image unavailable")
                    else:
                        st.write("Placeholder not found!")
            except Exception as e:
                st.write(f"Error with {name}: {str(e)}")
                if os.path.exists(placeholder_path):
                    try:
                        st.image(placeholder_path, width=125, caption="Image unavailable")
                    except Exception as pe:
                        st.write(f"Placeholder error: {str(pe)}")
                else:
                    st.write("Placeholder not found!")

            # Add a hidden button to capture the click
            if st.button("", key=f"select_{name}", on_click=lambda n=name: st.session_state.update(selected_casino=n), help="Hidden button"):
                pass  # The on_click callback handles the session state update

            # Close the logo-button container
            st.markdown('</div>', unsafe_allow_html=True)

            # Text button below the logo (opens URL in new tab)
            st.markdown(
                f"""
                <div class="text-button-container">
                    <a href="{url}" target="_blank" style="text-decoration: none;">
                        <div class="casino-button">
                            {name}
                        </div>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Close the container div
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.write("No casinos yet—check back soon!")