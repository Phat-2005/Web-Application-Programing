from flask import Flask, render_template, abort

app = Flask(__name__)

# Menu dictionary
menu = {
    "drinks": [
        {"name": "Coffee", "price": 2},
        {"name": "Juice", "price": 3}
    ],
    "food": [
        {"name": "Burger", "price": 5},
        {"name": "Pizza", "price": 8},
    ]
}

@app.route('/menu/<category>')
def show_menu(category):
    if category in menu:
        items = menu[category]
        return render_template('menu.html', category=category, items=items)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5016)
