from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global task list (in-memory)
tasks = [
    {"task": "Study", "completed": False},
    {"task": "Exercise", "completed": True}
]

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks.append({"task": new_task, "completed": False})
        return redirect(url_for('todo'))
    return render_template('todolist.html', tasks=tasks)

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True, port=5015)
