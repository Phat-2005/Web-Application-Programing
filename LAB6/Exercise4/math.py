from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('math.html')

@app.route('/square', methods=['POST'])
def square():
    try:
        num = int(request.form['number'])
        result = num ** 2
        return render_template('result.html', num=num, result=result)
    except:
        return "Invalid input. Please enter a valid number."

if __name__ == '__main__':
    app.run(debug=True, port=5003)
