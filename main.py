from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def title():
    return "Миссия Колонизация Марса"


@app.route("/index")
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def advertising_campaign():
    names = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!",
             ]
    return "<br><br>".join(names)


@app.route("/image_mars")
def image_mars():
    source = f'''<!doctype html>
                <html lang="en">
                <head>
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1><br>
                    <img src="{url_for("static", filename="IMAGES/Mars.jpg")}" alt="изображение марса" width=600>
                    <h4>Вот она какая, красная планета</h4>
                </body>
                </html>
            '''
    return source


@app.route("/promotion_image")
def promotion_image():
    return ...


@app.route("/astronaut_selection", method=['POST', 'GET'])
def astronaut_selection():
    return render_template("image_mars.html", CSSFILE="static/CSS/index.css")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
