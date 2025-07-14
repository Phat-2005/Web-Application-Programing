from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('score.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    physics = request.form['physics']
    chemistry = request.form['chemistry']
    maths = request.form['maths']
    return render_template('result.html', name=name, physics=physics, chemistry=chemistry, maths=maths)

if __name__ == '__main__':
    app.run(debug=True, port=5004)
