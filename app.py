from flask import Flask, render_template, redirect, request, url_for, redirect
from tweet import phrase
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("web.html")

@app.route('/', methods=["POST","GET"])
def web():
    if request.method == "POST":
          text = request.form["tweet"]
          
          return phrase(text)
    else:
        return render_template("web.html")       
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
