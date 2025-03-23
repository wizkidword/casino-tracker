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

def save_casinos(casinos):
    with open(CASINO_FILE, 'w') as f:
        json.dump(casinos, f, indent=4)

def save_casino_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

casinos = load_casinos()
casino_data = load_casino_data()

CASINO_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Social Casino Tracker</title>
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
            text-align: center;
        }
        .sidebar h2 {
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        .sidebar h3 {
            font-size: 1.2em;
            margin: 20px 0 10px;
        }
        .sidebar p {
            margin: 10px 0;
        }
        .sidebar form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            text-align: left;
        }
        .sidebar input[type="text"] {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1em;
        }
        .sidebar input[type="submit"] {
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .sidebar input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .sidebar ul {
            list-style: none;
            padding: 0;
            text-align: left;
            margin-top: 10px;
        }
        .sidebar ul li {
            margin: 5px 0;
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
        .top-forms {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            justify-content: center;
        }
        .top-forms form {
            display: flex;
            gap: 10px;
        }
        input[type="text"], input[type="url"], select {
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ddd;
            border-radius: 5px;
            flex: 1;
        }
        input[type="submit"] {
            padding: 10px 20px;
            font-size: 1em;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .delete-form input[type="submit"] {
            background-color: #dc3545;
        }
        .delete-form input[type="submit"]:hover {
            background-color: #b02a37;
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
            <p><strong>URL:</strong> <a href="{{ casinos[selected_casino] }}" target="_blank">{{ casinos[selected_casino] }}</a></p>
            <h3>Big Wins</h3>
            <form method="POST" action="/update_big_win">
                <input type="hidden" name="casino_name" value="{{ selected_casino }}">
                <input type="text" name="win_date" placeholder="Date (e.g., 2025-03-22)">
                <input type="text" name="bet_amount" placeholder="Bet (e.g., $5)">
                <input type="text" name="winnings" placeholder="Winnings (e.g., $100)">
                <input type="submit" value="Save">
            </form>
            {% if casino_data.get(selected_casino, {}).get('big_wins', []) %}
                <ul>
                    {% for win in casino_data[selected_casino]['big_wins'] %}
                        <li>{{ win['date'] }}: Bet {{ win['bet_amount'] }}, Won {{ win['winnings'] }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            <h3>Cash Outs</h3>
            <form method="POST" action="/update_data">
                <input type="hidden" name="casino_name" value="{{ selected_casino }}">
                <input type="text" name="cashout_date" placeholder="Date (e.g., 2025-03-22)">
                <input type="text" name="cashout_amount" placeholder="Amount (e.g., $50)">
                <input type="submit" value="Save">
            </form>
            {% if casino_data.get(selected_casino, {}).get('cashouts', []) %}
                <ul>
                    {% for cashout in casino_data[selected_casino]['cashouts'] %}
                        <li>{{ cashout['date'] }}: {{ cashout['amount'] }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% else %}
            <p>Select a casino to view details.</p>
        {% endif %}
    </div>
    <div class="main-content">
        <h1>Social Casino Tracker</h1>
        <div class="top-forms">
            <form method="POST" action="/add">
                <input type="text" name="name" placeholder="Casino Name" required>
                <input type="url" name="url" placeholder="Casino URL" required>
                <input type="submit" value="Add">
            </form>
            <form method="POST" action="/delete" class="delete-form">
                <select name="casino_to_delete">
                    {% for name in casinos.keys() %}
                        <option value="{{ name }}">{{ name }}</option>
                    {% endfor %}
                </select>
                <input type="submit" value="Delete">
            </form>
        </div>
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

@app.route('/add', methods=['POST'])
def add_casino():
    global casinos
    name = request.form['name']
    url = request.form['url']
    casinos[name] = url
    save_casinos(casinos)
    return redirect(url_for('casino_tracker'))

@app.route('/delete', methods=['POST'])
def delete_casino():
    global casinos, casino_data
    name = request.form['casino_to_delete']
    if name in casinos:
        del casinos[name]
        if name in casino_data:
            del casino_data[name]
        save_casinos(casinos)
        save_casino_data(casino_data)
    return redirect(url_for('casino_tracker'))

@app.route('/update_data', methods=['POST'])
def update_data():
    global casino_data
    casino_name = request.form['casino_name']
    new_cashout = {
        'date': request.form['cashout_date'],
        'amount': request.form['cashout_amount']
    }
    if casino_name not in casino_data:
        casino_data[casino_name] = {'cashouts': [], 'big_wins': []}
    elif 'cashouts' not in casino_data[casino_name]:
        casino_data[casino_name]['cashouts'] = []
    casino_data[casino_name]['cashouts'].append(new_cashout)
    save_casino_data(casino_data)
    return redirect(url_for('casino_tracker', selected=casino_name))

@app.route('/update_big_win', methods=['POST'])
def update_big_win():
    global casino_data
    casino_name = request.form['casino_name']
    new_win = {
        'date': request.form['win_date'],
        'bet_amount': request.form['bet_amount'],
        'winnings': request.form['winnings']
    }
    if casino_name not in casino_data:
        casino_data[casino_name] = {'cashouts': [], 'big_wins': []}
    elif 'big_wins' not in casino_data[casino_name]:
        casino_data[casino_name]['big_wins'] = []
    casino_data[casino_name]['big_wins'].append(new_win)
    save_casino_data(casino_data)
    return redirect(url_for('casino_tracker', selected=casino_name))

@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)