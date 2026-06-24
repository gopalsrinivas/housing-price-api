from fastapi import APIRouter, HTTPException

from app.schemas import HouseFeatures, BatchPrediction
from app.services.prediction_service import (
    predict_price,
    predict_batch_prices,
    get_model_information
)

router = APIRouter(tags=["Housing Prediction"])


@router.get("/")
async def root():

    return {
        "message": "Housing Price Prediction API"
    }


@router.get("/health")
async def health():

    return {
        "status": "UP"
    }


@router.post("/predict")
async def predict(data: HouseFeatures):

    try:

        result = predict_price(data)

        return {
            "predicted_price": result
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@router.post("/predict/batch")
async def batch_predict(data: BatchPrediction):

    try:

        result = predict_batch_prices(data)

        return {
            "predictions": result
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@router.get("/model-info")
async def model_info():

    try:

        return get_model_information()

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )