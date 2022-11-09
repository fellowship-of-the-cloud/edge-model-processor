# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pickle
import tarfile


if __name__ == '__main__':
    t = tarfile.open('model.tar.gz', 'r:gz')
    t.extractall()

    model_file_name = 'xgboost-model'
    with open(model_file_name, "rb") as input_file:
        e = pickle.load(input_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
