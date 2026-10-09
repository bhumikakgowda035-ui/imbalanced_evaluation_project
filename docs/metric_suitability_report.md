# Evaluation Metrics for Imbalanced Classification

## 1. Objective
This project evaluates a binary classifier on an imbalanced dataset and explains why accuracy alone can be misleading. The dataset is generated reproducibly with approximately 90% majority-class examples and 10% minority-class examples.

## 2. Business context
Imagine a fraud-screening service. Most transactions are legitimate, while only a small percentage are fraudulent. Missing fraud cases (false negatives) can be costly, but flagging legitimate transactions (false positives) also creates review work and customer friction.

## 3. Workflow
1. Generate an imbalanced binary dataset.
2. Split into training and testing data using stratification.
3. Train a baseline logistic-regression classifier without resampling or class weights.
4. Calculate confusion matrix, precision, recall, F1, ROC-AUC, and average precision.
5. Plot ROC and Precision-Recall curves.
6. Evaluate thresholds from 0.10 to 0.90.
7. Compare micro-, macro-, and weighted F1 scores.

## 4. Metric suitability
- **Precision** = TP / (TP + FP). Of the cases predicted positive, how many were truly positive?
- **Recall** = TP / (TP + FN). Of all actual positive cases, how many did the model find?
- **F1-score** = harmonic mean of precision and recall.
- **ROC-AUC** measures ranking quality across thresholds, but may look reassuring when the positive class is rare.
- **Average precision / PR curve** focuses on precision and recall for the positive class and is often more informative for rare-event detection.
- **Macro F1** calculates F1 for each class and gives each class equal weight.
- **Micro F1** aggregates true/false positives across classes; in ordinary single-label classification it equals accuracy.
- **Weighted F1** averages each class's F1 weighted by its support, so the majority class has more influence.

## 5. Threshold trade-off
Lowering the positive-class threshold usually increases recall but can reduce precision by creating more false positives. Raising it often improves precision but can miss more positive cases. The preferred threshold should reflect the relative business cost of false positives and false negatives, rather than automatically using 0.50.

## 6. Recommendation
For fraud detection, use **recall and Precision-Recall / average precision** as key measures when missed fraud is especially costly. Report precision alongside recall so operational teams understand the alert burden. Use ROC-AUC as a supplementary ranking metric and macro F1 to ensure minority-class performance is not hidden by the majority class. Select the threshold using validation data and business costs.

## 7. Limitations
This is a synthetic educational dataset, not real financial data. Results vary with the generated data and model. No single metric is best for every business problem; confirm the cost of false positives and false negatives with stakeholders.
