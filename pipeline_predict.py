import joblib
import pandas as pd
import numpy as np
import config as cfg

import my_preprocessors as mypp

survived_price_model = joblib.load('Survived_pipeline.pkl')

def predict(X):
    predicts = survived_price_model.predict(X)
    ypreds = predicts
    print(ypreds)
    return(ypreds[0])