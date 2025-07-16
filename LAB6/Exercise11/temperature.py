from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    result = None
    if request.method == 'POST':
        temp = request.form.get('temperature')
        conversion_type = request.form.get('conversion')

        try:
            temp = float(temp)
            if conversion_type == 'C to F':
                result = f"{temp} °C = {temp * 9/5 + 32:.2f} °F"
            elif conversion_type == 'F to C':
                result = f"{temp} °F = {(temp - 32) * 5/9:.2f} °C"
            else:
                result = "Invalid conversion type."
        except ValueError:
            result = "Please enter a valid number."

    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
