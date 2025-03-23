from flask import Flask, request, render_template_string, redirect, url_for
import json
import os

app = Flask(__name__)

CASINO_FILE = 'casinos.json'
DATA_FILE = 'casino_data.json'

def load_casinos():
    if os.path.exists(CASINO_FILE):
        with open(CASINO_FILE, 'r') as f:
            return json.load(f)
    return {
        "Slotomania": "https://www.slotomania.com/",
        "DoubleDown Casino": "https://www.doubledowncasino.com/",
    }

def load_casino_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

casinos = load_casinos()
casino_data = load_casino_data()

CASINO_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Best Free Social Casinos & Bonuses for 2025</title>
    <meta name="description" content="Explore the best free social casinos of 2025 with top bonuses, free games, and easy signups. Start playing now!">
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 40px;
            background-color: #ffffff;
            color: #333;
            display: flex;
        }
        .sidebar {
            width: 300px;
            padding: 20px;
            background-color: #f9f9f9;
            border-right: 1px solid #ddd;
            text-align: left;
        }
        .sidebar h2 {
            font-size: 1.5em;
            margin-bottom: 20px;
            text-align: center;
        }
        .sidebar p {
            margin: 10px 0;
        }
        .sidebar ul {
            list-style: none;
            padding: 0;
            margin-top: 10px;
        }
        .sidebar ul li {
            margin: 8px 0;
        }
        .main-content {
            flex: 1;
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            font-size: 2em;
            margin-bottom: 30px;
            color: #1a1a1a;
            text-align: center;
        }
        .casino-table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 100%;
        }
        .casino-table tr {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .casino-table td {
            padding: 15px;
            text-align: center;
            vertical-align: top;
            width: 150px;
            flex: 0 0 16.66%;
            box-sizing: border-box;
        }
        .casino-button {
            display: block;
            width: 125px;
            height: 125px;
            background-size: cover;
            background-position: center;
            border-radius: 10px;
            margin: 0 auto 10px;
            transition: transform 0.2s;
            cursor: pointer;
        }
        .casino-button:hover {
            transform: scale(1.05);
        }
        .casino-link {
            text-decoration: none;
            color: #007bff;
            font-size: 1em;
        }
        .casino-link:hover {
            color: #0056b3;
        }
        .empty-message {
            color: #666;
            font-style: italic;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="sidebar">
        {% if selected_casino %}
            <h2>{{ selected_casino }}</h2>
            <p><strong>Signup:</strong> <a href="{{ casinos[selected_casino] }}" target="_blank">Get Your Bonus Here</a></p>
            <ul>
                <li><strong>Free Daily SC:</strong> {{ casino_data.get(selected_casino, {}).get('free_daily_sc', 'N/A') }}</li>
                <li><strong>Daily Amount:</strong> {{ casino_data.get(selected_casino, {}).get('daily_amount', 'N/A') }}</li>
                <li><strong>Min. Cash Redeem:</strong> {{ casino_data.get(selected_casino, {}).get('min_cash_redeem', 'N/A') }}</li>
                <li><strong>Gift Cards:</strong> {{ casino_data.get(selected_casino, {}).get('gift_cards', 'N/A') }}</li>
                <li><strong>Crypto:</strong> {{ casino_data.get(selected_casino, {}).get('crypto', 'N/A') }}</li>
                <li><strong>VIP System:</strong> {{ casino_data.get(selected_casino, {}).get('vip_system', 'N/A') }}</li>
                <li><strong>Farm VIP w/GC:</strong> {{ casino_data.get(selected_casino, {}).get('farm_vip_with_gc', 'N/A') }}</li>
                <li><strong>Notes:</strong> {{ casino_data.get(selected_casino, {}).get('notes', 'No notes available.') }}</li>
            </ul>
        {% else %}
            <p>Select a casino to view details.</p>
        {% endif %}
    </div>
    <div class="main-content">
        <h1>Best Free Social Casinos & Bonuses for 2025</h1>
        {% if casinos %}
            <table class="casino-table">
                <tr>
                    {% for name, url in casinos.items() %}
                        <td>
                            <a href="/select/{{ name }}" class="casino-button" style="background-image: url('/static/{{ name|lower|replace(' ', '_') }}.png');"></a>
                            <a href="{{ url }}" target="_blank" class="casino-link">{{ name }}</a>
                        </td>
                        {% if loop.index is divisibleby 6 %}
                            </tr><tr>
                        {% endif %}
                    {% endfor %}
                </tr>
            </table>
        {% else %}
            <p class="empty-message">No casinos yet—add some!</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def casino_tracker():
    selected_casino = request.args.get('selected', None)
    return render_template_string(CASINO_TEMPLATE, casinos=casinos, casino_data=casino_data, selected_casino=selected_casino)

@app.route('/select/<casino_name>', methods=['GET'])
def select_casino(casino_name):
    return redirect(url_for('casino_tracker', selected=casino_name))

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)