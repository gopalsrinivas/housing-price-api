import pandas as pd

from app.model import model, metrics
from app.core.constants import FEATURE_COLUMNS


def predict_price(data):

    df = pd.DataFrame(
        [data.features],
        columns=FEATURE_COLUMNS
    )

    prediction = model.predict(df)

    return float(prediction[0])


def predict_batch_prices(data):

    df = pd.DataFrame(
        data.houses,
        columns=FEATURE_COLUMNS
    )

    predictions = model.predict(df)

    return predictions.tolist()


def get_model_information():

    return {
        "coefficients": model.coef_.tolist(),
        "intercept": float(model.intercept_),
        "r2_score": metrics["r2_score"],
        "mse": metrics["mse"],
        "feature_count": metrics["feature_count"]
    }