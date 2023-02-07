from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("root.html", CSSFILE="static/CSS/base.css")


@app.route("/index")
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route("/advertising_campaign")
def advertising_campaign():
    names = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!",
             ]
    return render_template("advertising_campaign.html", names=names)


@app.route("/image_mars")
def image_mars():
    return render_template("image_mars.html", FILE_IMAGE="Mars.jpg")


@app.route("/promotion_image")
def promotion_image():
    return ...


@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html", CSSFILE="static/CSS/astronaut_selection.css")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
