import pandas as pd
import joblib
import json

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("data/housing.csv")

X = df.drop(["id", "price"], axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

joblib.dump(model, "app/trained_model.pkl")

metrics = {
    "r2_score": float(r2),
    "mse": float(mse),
    "feature_count": len(X.columns)
}

with open("app/metrics.json", "w") as f:
    json.dump(metrics, f)

print("Training Completed")
print(metrics)