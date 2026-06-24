# Housing Price Prediction API

A FastAPI-based Machine Learning API that predicts housing prices using a Linear Regression model trained with Scikit-Learn.

## Tech Stack

* Python 3.12+
* FastAPI
* Scikit-Learn
* Pandas
* Joblib
* Docker

---

## Features

* Single House Price Prediction
* Batch House Price Prediction
* Model Information Endpoint
* Health Check Endpoint
* Swagger/OpenAPI Documentation
* Input Validation using Pydantic
* Docker Support

---

## Project Structure

```text
housing-price-api/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   │
│   ├── routers/
│   │   └── prediction_router.py
│   │
│   ├── services/
│   │   └── prediction_service.py
│   │
│   ├── core/
│   │   ├── constants.py
│   │   └── exceptions.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── trained_model.pkl
│   └── metrics.json
│
├── data/
│   └── housing.csv
│
├── tests/
│   └── test_prediction.py
│
├── train.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd housing-price-api
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux / Mac:

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train Model

Generate the trained model and metrics file:

```bash
python train.py
```

Expected Output:

```text
Training Completed
{
  "r2_score": 0.98,
  "mse": 105617714.99,
  "feature_count": 7
}
```

---

## Run Application

```bash
python -m uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

---

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "UP"
}
```

---

### Single Prediction

```http
POST /predict
```

Request:

```json
{
  "features": [
    1550,
    3,
    2,
    1997,
    6800,
    4.1,
    7.6
  ]
}
```

Response:

```json
{
  "predicted_price": 258061.41
}
```

---

### Batch Prediction

```http
POST /predict/batch
```

Request:

```json
{
  "houses": [
    [1550,3,2,1997,6800,4.1,7.6],
    [2200,4,2.5,2008,9600,7,8.8]
  ]
}
```

Response:

```json
{
  "predictions": [
    258061.41,
    366023.17
  ]
}
```

---

### Model Information

```http
GET /model-info
```

Response:

```json
{
  "coefficients": [],
  "intercept": 0,
  "r2_score": 0.98,
  "mse": 105617714.99,
  "feature_count": 7
}
```

---

## Docker

### Build Image

```bash
docker build -t housing-price-api .
```

### Run Container

```bash
docker run -p 8000:8000 housing-price-api
```

Application:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Author

Gopala Srinivas

Senior Software Developer
