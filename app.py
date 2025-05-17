from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def index():
    message = "Стартовое сообщение"
    if request.method == "POST":
        message = "Получен пост запрос"
    return render_template("index.html", message=message)


app.run()
