import tarfile

import numpy as np
import xgboost
import pandas


def check_instrument(instrument_values):
    t = tarfile.open('model.tar.gz', 'r:gz')
    t.extractall()

    model_file_name = 'xgboost-model'
    with open(model_file_name, "rb") as input_file:
        model = xgboost.Booster()
        model.load_model(model_file_name)
        data = pandas.DataFrame(np.arange(12).reshape((4, 3)), columns=instrument_values)
        xgb_matrix = xgboost.DMatrix(data)

        prediction = model.predict(xgb_matrix)

        return prediction
