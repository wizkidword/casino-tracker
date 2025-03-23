from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template
CALC_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Calculator</title></head>
<body>
    <h1>Calculator</h1>
    <form method="POST">
        <input type="number" name="num1" placeholder="First number" required>
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">×</option>
            <option value="divide">÷</option>
        </select>
        <input type="number" name="num2" placeholder="Second number" required>
        <input type="submit" value="Calculate">
    </form>
    {% if result is not none %}
        <p>{{ num1 }} {{ op_symbol }} {{ num2 }} = {{ result }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    num1 = num2 = op_symbol = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == 'add':
            result = num1 + num2
            op_symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            op_symbol = '-'
        elif operation == 'multiply':
            result = num1 * num2
            op_symbol = '×'
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                op_symbol = '÷'
            else:
                result = "Error: Division by zero!"
        
    return render_template_string(CALC_TEMPLATE, result=result, num1=num1, num2=num2, op_symbol=op_symbol)

if __name__ == '__main__':
    app.run(debug=True) 