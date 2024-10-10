import pickle

import numpy as np


def process(scaled_area):
    with open("./models/Ir_model.pkl", "rb") as f:
        regressor = pickle.load(f)
    predicted_cost = regressor.predict(scaled_area)

    with open("./models/scaler_y.pkl", "rb") as f:
        min_max_scaler_y = pickle.load(f)
    cost = np.round(min_max_scaler_y.inverse_transform([predicted_cost])[0][0], 2)

    return cost


def preprocess(area):
    with open("./models/scaler_x.pkl", "rb") as f:
        min_max_scaler_x = pickle.load(f)

    scaled_area = min_max_scaler_x.transform([[area]])
    return scaled_area