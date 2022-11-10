from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS, cross_origin

from model import instrument_predictor

app = Flask(__name__)
CORS(app)

# test: http://localhost:5000/api/mllab/check-instrument?time=10:15&dayOfWeek=Monday&instrumentId=1&num_samples_t0=51&num_samples_t15=48&num_samples_t30=53&num_samples_t45=61
# /api/mllab/check-instrument?time=10:15&dayOfWeek=Monday&instrumentId=1&num_samples_t0=51&num_samples_t15=48&num_samples_t30=53&num_samples_t45=61
@app.route("/api/mllab/check-instrument", methods=['GET'])
# TODO: change method to POST, GET is just for demo purposes in Browser.
def api_evaluate_instrument():

    time_a = request.args.get('time')
    day_of_week = request.args.get('dayOfWeek')
    instrument_id = request.args.get('instrumentId')
    num_samples_t0 = request.args.get('num_samples_t0')
    num_samples_t15 = request.args.get('num_samples_t15')
    num_samples_t30 = request.args.get('num_samples_t30')
    num_samples_t45 = request.args.get('num_samples_t45')

    result = instrument_predictor.check_instrument(time_a, day_of_week, instrument_id, num_samples_t0,
                                                   num_samples_t15, num_samples_t30, num_samples_t45)

    return str(result)


@app.route("/")
def home():
    return render_template('home.html')
    # return 'Roche LIS ML Autoconf API'


if __name__ == '__main__':
    #app.run()
    app.run(debug=False, host='0.0.0.0', port=5000)
