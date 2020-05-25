import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/helloWorld")
def helloWorld():
    return "Hello World!"

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/shuffle")
def shuffle():
    randNum = random.randint(1, 100)
    return render_template("number.html", number=randNum)

@app.route("/flipCoin")
def flipCoin():
    val = random.randint(0, 1)
    return render_template("toss.html", toss=val) 

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add_task.html")
    else:
        todo = request.form.get("task")         
        todos.append(todo)
        return redirect("/")

@app.route("/submit")
def submit():
    name = request.args.get("name")
    if not name:
        return render_template("failure.html")
    return render_template("name.html", name=name)
