'''This module defines a function to calculate classification metrics (F1 score, precision, and recall) for a given set of true labels and predicted labels. The function returns these metrics encapsulated in a ClassificationMetricArtifact object. It also includes error handling to raise a custom exception in case of any issues during the metric calculation process.'''

from sklearn.metrics import f1_score, precision_score, recall_score
import sys

from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException


def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:

    try:
        # =========================
        # Compute Metrics
        # =========================
        model_f1_score = f1_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)

        # =========================
        # Create Artifact
        # =========================
        classification_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score=model_recall_score
        )

        return classification_metric

    except Exception as e:
        raise NetworkSecurityException(e, sys)