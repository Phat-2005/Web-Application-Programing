from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def equation():
    return render_template('Ex3.html')

if __name__ == '__main__':

    app.run(debug=True)
