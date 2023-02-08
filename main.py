from flask import Flask, url_for, render_template, request, redirect
from DATA import list_professions
import os

app = Flask(__name__)

PATH_GALERY_IMAGE = "/home/bulat/PycharmProjects/FLASK/static/IMAGES/GALERY"
content = os.listdir(PATH_GALERY_IMAGE)

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


@app.route("/image_mars/")
def image_mars():
    return render_template("image_mars.html", FILE_IMAGE="Mars.jpg")


@app.route("/promotion_image")
def promotion_image():
    return ...


@app.route("/astronaut_selection/", methods=["GET", 'POST'])
def astronaut_selection():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        education = request.form['education']
        profession = request.form['profession']
        sex = request.form['gender']
        motivation = request.form['motivation']
        readiness = request.form['readiness']
        return answer_form(name=name, surname=surname, email=email, education=education, profession=profession, sex=sex,
                           motivation=motivation, readiness=readiness)
    return render_template("astronaut_selection.html", CSSFILE="/static/CSS/astronaut_selection.css")


@app.route("/galery/", methods=["POST", "GET"])
def galery():
    global content
    if request.method == "POST":
        file = request.files["photo"]
        if file.filename != "":
            file.save(os.path.join(PATH_GALERY_IMAGE, file.filename))
            content = os.listdir(PATH_GALERY_IMAGE)
    FILE_IMAGE = content[0]
    return redirect(f"/galery/{FILE_IMAGE}")


@app.route("/galery/<FILE_IMAGE>")
def galery_image(FILE_IMAGE):
    i = content.index(FILE_IMAGE)
    LEFT_LINK = content[i - 1]
    RIGHT_LINK = content[(i + 1) % len(content)]
    return render_template("galery.html", FILE_IMAGE=FILE_IMAGE, LEFT_LINK=LEFT_LINK, RIGHT_LINK=RIGHT_LINK,
                           CSSFILE='galery.css')


@app.route('/list_prof/<string:tag>/')
def list_prof(tag):
    return render_template("list_prof.html", professions=list_professions, tag=tag)


def answer_form(name, surname, email, education, profession, sex, motivation, readiness):
    if readiness == "on":
        readiness = "true"
    else:
        readiness = "false"
    return render_template("auto_answer.html", name=name, surname=surname, email=email, education=education,
                           profession=profession, sex=sex, motivation=motivation, readiness=readiness,
                           CSSFILE='/static/CSS/auto_answer.css')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
