from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<p>Hello</p><h1>Заголовок</h1>"


app.run()
