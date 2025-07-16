from flask import Flask, render_template, abort

app = Flask(__name__)

faqs = {
    1: {"question": "What is Flask?", "answer": "A web framework for Python."},
    2: {"question": "What is a route?", "answer": "A URL pattern used to call a function."}
}

@app.route('/faq/<int:question_id>')
def faq(question_id):
    if question_id in faqs:
        return render_template('faq.html', faq=faqs[question_id])
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5021)
