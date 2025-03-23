from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []  # Simple in-memory list

# HTML template
TODO_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>To-Do List</title></head>
<body>
    <h1>To-Do List</h1>
    <form method="POST">
        <input type="text" name="task" placeholder="Add a task" required>
        <input type="submit" value="Add">
    </form>
    <ul>
    {% for task in tasks %}
        <li>{{ task }}</li>
    {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template_string(TODO_TEMPLATE, tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)