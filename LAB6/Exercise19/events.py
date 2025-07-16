from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = [
    {"name": "Meeting", "date": "2025-08-01"},
    {"name": "Workshop", "date": "2025-08-10"}
]

@app.route('/events', methods=['GET', 'POST'])
def show_events():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        if name and date:
            events.append({"name": name, "date": date})
        return redirect(url_for('show_events'))
    return render_template('events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5018)
