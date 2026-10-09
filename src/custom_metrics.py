"""Custom evaluation metrics and plotting for imbalanced binary classification."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    roc_curve, precision_recall_curve, roc_auc_score, average_precision_score,
    confusion_matrix, precision_score, recall_score, f1_score,
    f1_score as sklearn_f1_score
)

def calculate_metrics(y_true, y_prob, threshold=0.5):
    """Calculate binary classification metrics at a chosen probability threshold."""
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    y_pred = (y_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        "threshold": float(threshold),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_true, y_prob),
        "average_precision": average_precision_score(y_true, y_prob),
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }

def plot_roc_curve(y_true, y_prob, output_path=None):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    auc = roc_auc_score(y_true, y_prob)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"ROC AUC = {auc:.3f}")
    ax.plot([0, 1], [0, 1], linestyle="--", label="Random baseline")
    ax.set(xlabel="False Positive Rate", ylabel="True Positive Rate",
           title="ROC Curve")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.tight_layout()
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150)
    return fig

def plot_precision_recall_curve(y_true, y_prob, output_path=None):
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    ap = average_precision_score(y_true, y_prob)
    fig, ax = plt.subplots()
    ax.plot(recall, precision, label=f"Average precision = {ap:.3f}")
    ax.set(xlabel="Recall", ylabel="Precision",
           title="Precision-Recall Curve")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.tight_layout()
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150)
    return fig
