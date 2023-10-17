from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/hat")
def hat_page():
    return render_template("hat.html")

@app.route("/jumper")
def jumper_page():
    return render_template("jumper.html")

@app.route("/shoes")
def shoes_page():
    return render_template("shoes.html")

@app.route("/submit", methods = ["POST"])
def submit():
    input_name = request.form.get("name")
    input_email = request.form.get("email")
    input_message = request.form.get("message")
    return render_template("form.html", name = input_name, email = input_email, message = input_message)