from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def login():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'patkarC.jpg')
    return render_template("login.html",user_image=pic1)

@app.route("/register")
def register():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'patkarC.jpg')
    return render_template("register.html",user_image=pic1)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/ej")
def ej():
    return render_template("ej.html")

@app.route("/awp")
def awp():
    return render_template("awp.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

@app.route("/spm")
def spm():
    return render_template("spm.html")

@app.route("/iot")
def iot():
    return render_template("iot.html")

@app.route("/generalNews")
def generalNews():
    return render_template("generalnews.html")

@app.route("/generalNews1")
def generalNews1():
    return render_template("generalnews1.html")

@app.route("/generalNews2")
def generalNews2():
    return render_template("generalnews2.html")

if __name__ == "__main__":
    app.run(debug=True)