# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tarfile

import numpy as np
import xgboost
import pandas

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

if __name__ == '__main__':
    t = tarfile.open('model.tar.gz', 'r:gz')
    t.extractall()

    model_file_name = 'xgboost-model'
    with open(model_file_name, "rb") as input_file:
        model = xgboost.Booster()
        model.load_model(model_file_name)

        df = pandas.DataFrame([
            {
                "readmitted": 'no',
                "race": 'african_american',
                "gender": 'female',
                "age": 25,
                "time_in_hospital": 2,
                "num_lab_procedures": 11,
                "num_procedures": 5,
                "num_medications": 13,
                "number_outpatient": 2,
                "number_emergency": 0,
                "number_inpatient": 1,
                "number_diagnoses": 6,
                "max_glu_serum": 'none',
                "a1c_result": 'none',
                "change": 0,
                "diabetes_med": 1
            }
        ])

        # extract the features and target
        X_test = df

        # one-hot encode the categorical features
        cat_attribs = ['readmitted', 'race', 'gender', 'max_glu_serum', 'a1c_result']
        full_pipeline = ColumnTransformer([('cat', OneHotEncoder(handle_unknown='ignore'), cat_attribs)],
                                          remainder='passthrough')

        encoder = full_pipeline.fit(X_test)
        X_test_e = encoder.transform(X_test)



        dtrain = xgboost.DMatrix(X_test_e )

       # print(model.get_params(deep=True))


        print(model.predict(dtrain))
