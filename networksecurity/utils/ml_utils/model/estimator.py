'''This module defines the NetworkModel class, which serves as a wrapper for combining a preprocessor and a trained machine learning model. The class provides a predict method that applies the preprocessor to input data and generates predictions using the trained model. This design allows for seamless integration of preprocessing steps with model inference, making it easier to use the trained model for making predictions on new data. The module also includes error handling using a custom exception class to ensure that any issues are properly logged and raised.'''

import os
import sys

from networksecurity.constant.training_pipeline import (
    SAVED_MODEL_DIR,
    MODEL_FILE_NAME
)

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkModel:
    """Wrapper class that combines preprocessor and trained model for prediction."""

    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def predict(self, x):
        """Applies preprocessing and generates predictions using the trained model."""
        try:
            x_transformed = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transformed)
            return y_hat

        except Exception as e:
            raise NetworkSecurityException(e, sys)