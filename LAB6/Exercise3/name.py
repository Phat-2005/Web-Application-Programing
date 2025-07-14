from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('flask.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['nm']
    return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
    return f"welcome {name}"

if __name__ == '__main__':
    app.run(debug=True, port=5002)
