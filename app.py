from flask import Flask, render_template, redirect, request, url_for, redirect
from tweet import phrase

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("web.html")

@app.route('/web', methods=["POST","GET"])
def web():
    if request.method == "POST":
          text = request.form["tweet"]
          
          return phrase(text)
    else:
        return render_template("web.html")       
#@app.route("/result")
#def result(yourtext):
    #return {yourtext}


if __name__ == '__main__':
    app.run()
