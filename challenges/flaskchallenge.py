#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/correct")
def success():
    return f"Corrct!\n"

@app.route("/") # user can land at "/"
def start():
    return render_template("index.html") # look for templates/postmaker.html

@app.route("/send", methods = ["POST"])
def send():
    if request.method == "POST":
        if request.form.get("answer") == "african or european":
            fanswer = request.form.get("answer") #
            return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application

