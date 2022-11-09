# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tarfile

import numpy as np
import xgboost
import pandas

if __name__ == '__main__':
    t = tarfile.open('model.tar.gz', 'r:gz')
    t.extractall()

    model_file_name = 'xgboost-model'
    with open(model_file_name, "rb") as input_file:
        model = xgboost.Booster()
        model.load_model(model_file_name)

        secondrow = pandas.DataFrame()

        test_data = np.array(secondrow, dtype=float)

        data = pandas.DataFrame(np.arange(12).reshape((4, 3)), columns=['a', 'b', 'c'])
        dtrain = xgboost.DMatrix(data)


        model.predict(dtrain)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
