from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS, cross_origin

from model import instrument_predictor

app = Flask(__name__)
CORS(app)


@app.route("/api/mllab/check-instrument", methods=['GET'])
def api_evaluate_instrument():

    result = instrument_predictor.check_instrument(['a', 'b', 'c'])

    return str(result)


@app.route("/")
def home():
    return render_template('home.html')
    # return 'Roche LIS ML Autoconf API'


if __name__ == '__main__':
    #app.run()
    app.run(debug=False, host='0.0.0.0', port=5000)
