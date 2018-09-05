from flask import render_template, Flask
from FlaskApp.content_management import Content

app = Flask(__name__)

TOPIC_DICT = Content()


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT="AADAD")
    except Exception as e:
        return render_template("500.html", error=str(e))

