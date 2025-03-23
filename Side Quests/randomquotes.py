from flask import Flask, render_template_string
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Code is like humor. When you have to explain it, it’s bad. - Cory House",
    "Programming isn’t about what you know; it’s about what you can figure out. - Chris Pine",
]

# HTML template
QUOTE_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Quote Generator</title></head>
<body>
    <h1>Random Quote</h1>
    <p>{{ quote }}</p>
    <form method="POST">
        <input type="submit" value="New Quote">
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def quote():
    quote = random.choice(quotes)
    return render_template_string(QUOTE_TEMPLATE, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)