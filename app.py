import pickle
import numpy as np
from flask import Flask, render_template, request

model = pickle.load(open("model.pkl", 'rb'))
scale = pickle.load(open("scale.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods=['POST'])
def output():
    values = [float(x) for x in request.form.values()]
    scaled_values = scale.transform([values])
    output = model.predict(scaled_values)
    print(output)
    return render_template("output.html", output = "Price of the House is : {} " .format(np.abs(output[0])))


if __name__ == "__main__":
    app.run(debug=True)