from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample dictionary of blog posts
posts = {
    1: {"title": "First Post", "content": "Hello, world!"},
}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = posts.get(post_id)
    if post:
        return render_template('blog.html', title=post["title"], content=post["content"])
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5011)
