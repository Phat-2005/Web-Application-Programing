from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"title": "Doraemon", "author": "Fujiko Fujio"},
    {"title": "Transformers Skybound", "author": "Daniel Warren Johnson"}
]

@app.route('/books', methods=['GET', 'POST'])
def book_list():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        if title and author:
            books.append({"title": title, "author": author})
        return redirect(url_for('book_list'))
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True, port=5020)
