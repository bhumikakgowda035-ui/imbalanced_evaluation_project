# Imbalanced Classification Evaluation

A beginner-friendly Python project demonstrating custom metrics, ROC and Precision-Recall curves, threshold trade-offs, confusion matrix, and micro/macro/weighted F1 for an imbalanced dataset.

## Dataset and business context
The script generates a synthetic binary dataset with about 90% majority class and 10% minority class. The example business context is fraud screening: the minority class represents potentially fraudulent transactions. No external dataset download is needed.

## Project files
```text
README.md
requirements.txt
main.py
src/
  custom_metrics.py
docs/
  metric_suitability_report.md
results/                 # created when the script runs
```

## Setup (Windows / VS Code)
1. Install Python 3.10 or later.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```
5. Activate it:
   - PowerShell: `.venv\Scripts\Activate.ps1`
   - Command Prompt: `.venv\Scripts\activate.bat`
6. Install libraries:
   ```bash
   python -m pip install -r requirements.txt
   ```
7. Run:
   ```bash
   python main.py
   ```

If `python` is not recognized, try `py main.py` and `py -m pip install -r requirements.txt`.

## Outputs
The `results` folder is automatically created and contains:
- `confusion_matrix.png`
- `roc_curve.png`
- `precision_recall_curve.png`
- `threshold_metrics.csv`
- `metrics.json`

## How to complete the six assignment steps
1. **Choose an imbalanced dataset:** the script synthesizes a 90:10 binary dataset.
2. **Baseline classifier:** logistic regression is trained without resampling or class weighting.
3. **Custom metrics and plots:** `src/custom_metrics.py` computes metrics and plots ROC and Precision-Recall curves.
4. **Threshold analysis:** results for thresholds 0.10–0.90 are saved to `results/threshold_metrics.csv`.
5. **F1 comparison:** `main.py` calculates micro, macro, and weighted F1.
6. **Report:** read `docs/metric_suitability_report.md`; adapt the recommendation to your own business scenario.

## Push to GitHub
Create a new empty GitHub repository, then run these commands in the VS Code terminal from this folder:
```bash
git init
git add .
git commit -m "Add imbalanced evaluation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the URL with your own repository URL. Do not upload `.venv/` or private data.
