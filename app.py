from flask import Flask, render_template, request

from processing import process, preprocess


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        area = request.form.get("area")
        try:
            area = float(area)
        except:
            area = 0
            message += 'Некорректный ввод. Установлено значение по умалчанию.'
        scaled_area = preprocess(area)
        cost = process(scaled_area)
        message += f"Стоимость недвижимости {cost} рублей"
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()