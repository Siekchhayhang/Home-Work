from flask import Flask, render_template, request
app=Flask(__name__, static_url_path= "/static")

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("home.html")

@app.route("/siekchhaihang", methods=['GET','POST'])
def result():

    return render_template("data.html")

app.run(debug=True)