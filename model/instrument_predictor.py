import tarfile

import numpy as np
import xgboost
import pandas

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def check_instrument(time_a, day_of_week, instrument_id, num_samples_t0,
                     num_samples_t15, num_samples_t30, num_samples_t45):
    t = tarfile.open('model.tar.gz', 'r:gz')
    t.extractall()

    data = [
        {'Time': time_a,
         'TimeMinutes': 15,
         'DayOfWeek': day_of_week,
         'Monday': 1,
         'Tuesday': 0,
         'Wednesday': 0,
         'Thursday': 0,
         'Friday': 0,
         'Saturday': 0,
         'Sunday': 0,
         'InstrumentId': instrument_id,
         'num_samples_t0': num_samples_t0,
         'num_samples_t0-15': num_samples_t15,
         'num_samples_t0-30': num_samples_t30,
         'num_samples_t0-45': num_samples_t45
         },
    ];

    df = pandas.DataFrame(data)
    x_test = df
    cat_attribs = ['DayOfWeek']

    full_pipeline = ColumnTransformer([('cat', OneHotEncoder(handle_unknown='ignore'), cat_attribs)],
                                      remainder='passthrough')

    encoder = full_pipeline.fit(x_test)
    x_test_e = encoder.transform(x_test)
    xgb_matrix = xgboost.DMatrix(x_test_e)

    model_file_name = 'xgboost-model'
    with open(model_file_name, "rb") as input_file:
        model = xgboost.Booster()
        model.load_model(model_file_name)

        prediction = model.predict(xgb_matrix)
        print(prediction)
        return prediction[0]
