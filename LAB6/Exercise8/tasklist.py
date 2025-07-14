from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def tasklist():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect(url_for('tasklist'))
    return render_template('tasklist.html', tasks=tasks)

@app.route('/')
def home_redirect():
    return redirect(url_for('tasklist'))

if __name__ == '__main__':
    app.run(debug=True, port=5007)
