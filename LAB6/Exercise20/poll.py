from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votes = {"Cats": 0, "Dogs": 0}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form.get('vote')
        if choice in votes:
            votes[choice] += 1
        return redirect(url_for('poll'))

    total_votes = sum(votes.values())
    percentages = {
        option: (count / total_votes * 100) if total_votes else 0
        for option, count in votes.items()
    }

    return render_template('poll.html', votes=votes, percentages=percentages)

if __name__ == '__main__':
    app.run(debug=True, port=5019)
