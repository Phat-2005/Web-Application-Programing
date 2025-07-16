from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/color', methods=['GET', 'POST'])
def color():
    background_color = "white"  #default color
    if request.method == 'POST':
        user_color = request.form.get('color')
        if user_color:
            background_color = user_color
    return render_template('color.html', bg_color=background_color)

if __name__ == '__main__':
    app.run(debug=True, port=5012)
