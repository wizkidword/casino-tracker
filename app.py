import streamlit as st
import json
import os
from PIL import Image
import streamlit_analytics

# SEO-friendly title (must be the first Streamlit command)
st.set_page_config(
    page_title="Best Free Social Casinos & Bonuses for 2025",
    page_icon="🎰",
    layout="wide"
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

# Global CSS for logo hover effect and invisible button overlay
st.markdown(
    """
    <style>
    .casino-logo {
        position: relative;
        display: inline-block;
        width: 125px;
        height: 125px;
        cursor: pointer;
    }
    .casino-logo:hover {
        opacity: 0.8;
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

            # Invisible button overlay for click detection
            st.button("", key=f"select_{name}", on_click=lambda n=name: st.session_state.update({'selected_casino': n}))
            
            st.markdown(f"[{name}]({url})", unsafe_allow_html=True)
else:
    st.write("No casinos yet—check back soon!")