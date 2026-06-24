from pydantic import BaseModel, field_validator
from typing import List

from app.core.constants import EXPECTED_FEATURES


class HouseFeatures(BaseModel):
    features: List[float]

    @field_validator("features")
    @classmethod
    def validate_features(cls, value):

        if len(value) != EXPECTED_FEATURES:
            raise ValueError(
                f"Expected {EXPECTED_FEATURES} features"
            )

        return value


class BatchPrediction(BaseModel):
    houses: List[List[float]]

    @field_validator("houses")
    @classmethod
    def validate_houses(cls, value):

        for house in value:

            if len(house) != EXPECTED_FEATURES:
                raise ValueError(
                    f"Each house must contain {EXPECTED_FEATURES} features"
                )

        return value