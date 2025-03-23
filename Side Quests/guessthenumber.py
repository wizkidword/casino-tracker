from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

number = random.randint(1, 100)  # Random number to guess

# HTML template
GAME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Guess the Number</title></head>
<body>
    <h1>Guess a Number (1-100)</h1>
    <form method="POST">
        <input type="number" name="guess" min="1" max="100" required>
        <input type="submit" value="Guess">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def game():
    message = None
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < number:
            message = "Too low! Try again."
        elif guess > number:
            message = "Too high! Try again."
        else:
            message = f"Correct! The number was {number}. Refresh to play again."
    return render_template_string(GAME_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(debug=True)