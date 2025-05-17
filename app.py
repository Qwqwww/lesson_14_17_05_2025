from flask import Flask, render_template, request


from process import predict


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def index():
    message = "Пример сообщения"
    if request.method == "POST":
        area = request.form.get("area")

        # TODO: Добавить проверку ввода
        area = float(area)

        cost = predict(area)
        message = f"Стоимость недвижимости площадью {area} кв. м. равна {cost} руб."
    return render_template("index.html", message=message)
