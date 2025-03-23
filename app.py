import gradio as gr # type: ignore
import json
import os

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

# Google Analytics script
google_analytics = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RVJVWRK9BT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RVJVWRK9BT', { 'send_page_view': false });
  gtag('event', 'page_view', {
    page_title: document.title,
    page_location: window.location.href,
    page_path: window.location.pathname
  });
</script>
"""

# CSS for styling (adapted for Gradio)
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');

body {
    background-image: url('https://cdn.pixabay.com/photo/2013/12/12/22/11/game-casino-227586_1280.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    background-color: #1a1a1a; /* Fallback color */
}

body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6); /* Dark overlay with 60% opacity */
    z-index: -1;
}

h1, h2, h3, p, div, span, a {
    color: #f0f0f0 !important; /* Light gray/white text for readability */
}

h1, h2, h3 {
    font-family: 'Luckiest Guy', cursive !important;
    color: gold !important;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.casino-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}

.logo-button-container {
    position: relative;
    width: 125px;
    height: 125px;
    cursor: pointer;
}

.logo-button-container img {
    width: 125px;
    height: 125px;
    object-fit: contain;
    transition: all 0.3s ease;
    border: 2px solid gold;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.7);
    padding: 5px;
    box-sizing: border-box;
}

.logo-button-container img:hover {
    opacity: 1;
    box-shadow: 0 0 15px gold, 0 0 30px rgba(255, 215, 0, 0.5);
}

.text-button-container {
    z-index: 2;
}

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

#sidebar {
    background: linear-gradient(to bottom, #1a1a1a, #333333);
    padding: 10px;
    border-radius: 5px;
}

#sidebar * {
    color: gold !important;
}
</style>
"""

# Function to update the sidebar
def update_sidebar(casino_name):
    if casino_name and casino_name in casinos:
        return (
            f"<h2 style='text-align: center;'>{casino_name}</h2>"
            f"<p><b>Signup:</b> <a href='{casinos[casino_name]}' target='_blank'>Get Your Bonus Here</a></p>"
            f"<p><b>Free Daily SC:</b> {casino_data.get(casino_name, {}).get('free_daily_sc', 'N/A')}</p>"
            f"<p><b>Daily Amount:</b> {casino_data.get(casino_name, {}).get('daily_amount', 'N/A')}</p>"
            f"<p><b>Min. Cash Redeem:</b> {casino_data.get(casino_name, {}).get('min_cash_redeem', 'N/A')}</p>"
            f"<p><b>Gift Cards:</b> {casino_data.get(casino_name, {}).get('gift_cards', 'N/A')}</p>"
            f"<p><b>Crypto:</b> {casino_data.get(casino_name, {}).get('crypto', 'N/A')}</p>"
            f"<p><b>VIP System:</b> {casino_data.get(casino_name, {}).get('vip_system', 'N/A')}</p>"
            f"<p><b>Farm VIP w/GC:</b> {casino_data.get(casino_name, {}).get('farm_vip_with_gc', 'N/A')}</p>"
            f"<p><b>Notes:</b> {casino_data.get(casino_name, {}).get('notes', 'No notes available.')}</p>"
        )
    return "Select a casino to view details."

# Build the Gradio app
with gr.Blocks(css=css) as app:
    # Inject Google Analytics
    gr.HTML(google_analytics)

    # Title
    gr.Markdown("# Best Free Social Casinos & Bonuses for 2025")

    # Layout with sidebar and main content
    with gr.Row():
        # Sidebar
        with gr.Column(scale=1):
            sidebar = gr.HTML("Select a casino to view details.", elem_id="sidebar")

        # Main content (casino grid)
        with gr.Column(scale=5):
            if casinos:
                # Create a grid with 6 columns
                with gr.Row():
                    for i, (name, url) in enumerate(casinos.items()):
                        with gr.Column(scale=1, min_width=150):
                            # Casino container
                            gr.HTML('<div class="casino-container">', unsafe_allow_html=True)

                            # Logo (clickable)
                            logo_path = f"static/{name.lower().replace(' ', '_')}.png"
                            placeholder_path = "static/placeholder.png"
                            image_path = logo_path if os.path.exists(logo_path) else placeholder_path
                            gr.Image(
                                image_path,
                                width=125,
                                height=125,
                                interactive=True,
                                elem_classes="logo-button-container"
                            ).click(
                                fn=lambda n=name: update_sidebar(n),
                                outputs=sidebar
                            )

                            # Text button (opens URL in new tab)
                            gr.HTML(
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

                            gr.HTML('</div>', unsafe_allow_html=True)
            else:
                gr.Markdown("No casinos yet—check back soon!")

# Launch the app (for local testing)
app.launch()