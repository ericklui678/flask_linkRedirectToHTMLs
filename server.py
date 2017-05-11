from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/left')
def left():
    return render_template("left.html")

@app.route('/right')
def right():
    return render_template("right.html")

@app.route('/leftDoor')
def leftDoor():
    return render_template("leftDoor.html")

@app.route('/rightDoor')
def rightDoor():
    return render_template("rightDoor.html")


app.run(debug = True)
