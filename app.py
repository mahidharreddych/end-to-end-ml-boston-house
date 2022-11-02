import pickle
from flask import Flask, render_template, request

model = pickle.load(open("model.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction")
def output():
    return render_template("output.html")


if __name__ == "__main__":
    app.run(debug=True)