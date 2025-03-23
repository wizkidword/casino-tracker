import streamlit as st
import json
import os
from PIL import Image

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
    </style>
    """,
    unsafe_allow_html=True
)

# Add Google Analytics tracking code manually
st.components.v1.html(
    """
    <script>
      // Wait for the page to load before injecting the Google Analytics script
      window.onload = function() {
        setTimeout(function() {
          // Create the gtag.js script tag
          var gtagScript = document.createElement('script');
          gtagScript.async = true;
          gtagScript.crossorigin = 'anonymous';
          gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-RVJVWRK9BT';
          document.head.appendChild(gtagScript);

          // Create the gtag config script
          var configScript = document.createElement('script');
          configScript.innerHTML = `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-RVJVWRK9BT', { 'send_page_view': false });
            if (typeof gtag !== 'function') {
              console.log('Google Analytics failed to load');
            }

            // Manually send a page view on initial load
            gtag('event', 'page_view', {
              page_title: document.title,
              page_location: window.location.href,
              page_path: window.location.pathname
            });

            // Listen for Streamlit messages to detect state changes
            window.addEventListener('message', function(event) {
              if (event.data && event.data.type === 'streamlit:set_component_value') {
                gtag('event', 'page_view', {
                  page_title: document.title,
                  page_location: window.location.href + '?selected=' + (event.data.value || 'none'),
                  page_path: window.location.pathname + '?selected=' + (event.data.value || 'none')
                });
              }
            });
          `;
          document.head.appendChild(configScript);
        }, 1000);
      };
    </script>
    """,
    height=0
)

# File paths
CASINO_FILE = 'casinos.json'
DATA_FILE = 'casino_data.json'

# Load casino data
def load_casinos():
    if os.path.exists(CASINO_FILE):
        with open(CASINO_FILE, 'r') as f:
            return json.load(f)
    return {
        "Slotomania": "https://www.slotomania.com/?ref=your_ref_link",
        "DoubleDown Casino": "https://www.doubledowncasino.com/?ref=your_ref_link",
    }

def load_casino_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

casinos = load_casinos()
casino_data = load_casino_data()

# Main content
st.title("Best Free Social Casinos & Bonuses for 2025")

# Sidebar with centered title
with st.sidebar:
    selected_casino = st.session_state.get('selected_casino', None)

    if selected_casino and selected_casino in casinos:
        # Center the header with CSS
        st.markdown(
            f"<h2 style='text-align: center;'>{selected_casino}</h2>",
            unsafe_allow_html=True
        )
        st.write(f"**Signup:** [Get Your Bonus Here]({casinos[selected_casino]})")
        st.write(f"**Free Daily SC:** {casino_data.get(selected_casino, {}).get('free_daily_sc', 'N/A')}")
        st.write(f"**Daily Amount:** {casino_data.get(selected_casino, {}).get('daily_amount', 'N/A')}")
        st.write(f"**Min. Cash Redeem:** {casino_data.get(selected_casino, {}).get('min_cash_redeem', 'N/A')}")
        st.write(f"**Gift Cards:** {casino_data.get(selected_casino, {}).get('gift_cards', 'N/A')}")
        st.write(f"**Crypto:** {casino_data.get(selected_casino, {}).get('crypto', 'N/A')}")
        st.write(f"**VIP System:** {casino_data.get(selected_casino, {}).get('vip_system', 'N/A')}")
        st.write(f"**Farm VIP w/GC:** {casino_data.get(selected_casino, {}).get('farm_vip_with_gc', 'N/A')}")
        st.write(f"**Notes:** {casino_data.get(selected_casino, {}).get('notes', 'No notes available.')}")
    else:
        st.write("Select a casino to view details.")

# Global CSS for logo hover effect, invisible button overlay, and text buttons
st.markdown(
    """
    <style>
    .casino-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px; /* Add space between rows */
    }
    .casino-logo {
        position: relative;
        display: inline-block;
        width: 125px;
        height: 125px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid gold;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 5px;
    }
    .casino-logo:hover {
        opacity: 1;
        box-shadow: 0 0 15px gold, 0 0 30px rgba(255, 215, 0, 0.5);
    }
    div[data-testid="stButton"] button {
        position: absolute;
        top: -125px;
        left: 0;
        width: 125px;
        height: 125px;
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        cursor: pointer;
    }
    div[data-testid="stButton"] button:hover {
        background: rgba(0, 0, 0, 0.1) !important;
    }
    div[data-testid="stButton"] button:focus {
        outline: none !important;
        box-shadow: none !important;
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
        margin-top: 10px; /* Increased space between logo and button */
    }
    .casino-button:hover {
        background-color: rgba(255, 215, 0, 0.2);
        box-shadow: 0 0 10px gold;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
            
            # Load image
            try:
                if os.path.exists(logo_path):
                    img = Image.open(logo_path)
                    st.image(img, width=125, use_container_width=False)
                else:
                    st.write(f"Logo not found: {logo_path}")
                    if os.path.exists(placeholder_path):
                        placeholder = Image.open(placeholder_path)
                        st.image(placeholder, width=125, use_container_width=False, caption="Image unavailable")
                    else:
                        st.write("Placeholder not found!")
            except Exception as e:
                st.write(f"Error with {name}: {str(e)}")
                if os.path.exists(placeholder_path):
                    try:
                        placeholder = Image.open(placeholder_path)
                        st.image(placeholder, width=125, use_container_width=False, caption="Image unavailable")
                    except Exception as pe:
                        st.write(f"Placeholder error: {str(pe)}")
                else:
                    st.write("Placeholder not found!")

            # Invisible button overlay for click detection (logo click to update sidebar)
            st.button("", key=f"select_{name}", on_click=lambda n=name: st.session_state.update({'selected_casino': n}))

            # Styled text button below the logo (only opens URL in new tab)
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div class="casino-button">
                        {name}
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
            
            # Close the container div
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.write("No casinos yet—check back soon!")