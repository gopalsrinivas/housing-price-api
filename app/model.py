import os
import json
import joblib
import subprocess

MODEL_PATH = "app/trained_model.pkl"
METRICS_PATH = "app/metrics.json"

if not os.path.exists(MODEL_PATH):
    subprocess.run(["python", "train.py"])

model = joblib.load(MODEL_PATH)

with open(METRICS_PATH, "r") as file:
    metrics = json.load(file)