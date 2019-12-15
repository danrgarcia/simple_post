from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_post, create_post

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form['name']
        post = request.form['post']
        create_post(name, post)

    posts = get_post()
    print(posts)

    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
