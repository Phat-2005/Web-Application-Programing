from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

quotes = [
    "Optimism is more associated with success and happiness than anything else.",
    "Always keep your eyes open and look around. Because whatever you see can inspire you.",
    "I destroy my enemies by making them friends.",
    "Success is not in what you have, but who you are."
]

@app.route('/quote')
def show_quote():
    quote = random.choice(quotes)
    return render_template('quote.html', quote=quote)

@app.route('/new-quote')
def new_quote():
    return redirect(url_for('show_quote'))

if __name__ == '__main__':
    app.run(debug=True, port=5017)
