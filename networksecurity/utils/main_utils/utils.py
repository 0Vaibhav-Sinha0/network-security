'''This module contains utility functions for the network security project, including operations for reading and writing YAML files, saving and loading NumPy arrays, serializing and deserializing Python objects, and evaluating machine learning models. These utilities are designed to support various components of the project by providing common functionalities that can be reused across different stages of the machine learning pipeline. The module also includes error handling using a custom exception class to ensure that any issues are properly logged and raised.'''

import os
import sys
import yaml
import pickle
import numpy as np

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# =========================
# YAML Operations
# =========================

def read_yaml_file(file_path: str) -> dict:
    """Reads a YAML file and returns its content as a dictionary."""
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """Writes content to a YAML file, optionally replacing existing file."""
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys)


# =========================
# NumPy Operations
# =========================

def save_numpy_array_data(file_path: str, array: np.array):
    """Saves a NumPy array to a binary file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """Loads a NumPy array from a binary file."""
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


# =========================
# Object Serialization
# =========================

def save_object(file_path: str, obj: object) -> None:
    """Serializes and saves a Python object using pickle."""
    try:
        logging.info("Saving object...")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info("Object saved successfully.")

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def load_object(file_path: str) -> object:
    """Loads and deserializes a Python object using pickle."""
    try:
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


# =========================
# Model Evaluation
# =========================

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """Performs hyperparameter tuning and evaluates multiple models using R2 score."""
    try:
        report = {}

        for i in range(len(models)):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            para = param[model_name]

            # Hyperparameter tuning
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # Train with best params
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score

        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)