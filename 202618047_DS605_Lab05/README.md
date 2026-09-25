# DS605 Lab 05: Machine Learning with Scikit-learn and From Scratch

## Overview

This lab implements regression and classification models using Scikit-learn and recreates the workflow manually using NumPy and Pandas.

The models are evaluated using predictive performance metrics and execution time.

## Dataset

* **Dataset:** Productivity Prediction of Garment Employees
* **File:** `garments_worker_productivity.csv`

## Objectives

* Predict actual productivity using Linear Regression.
* Predict whether a worker meets the productivity target using Logistic Regression.
* Implement preprocessing and model training manually using NumPy and Pandas.
* Compare model performance and execution time.
* Optimize the manual Logistic Regression model.

## Models

### 1. Regression

* **Target:** `actual_productivity`
* **Model:** Linear Regression

### 2. Classification

* **Target:** `MeetsTarget`
* **Definition:** 1 if `actual_productivity >= targeted_productivity`, otherwise 0.
* **Model:** Logistic Regression

The `actual_productivity` feature is excluded from classification inputs to prevent target leakage.

## Implementation

### Part A — Scikit-learn

* Missing-value imputation
* Categorical feature encoding
* Feature scaling
* Fixed train-test split
* Linear Regression
* Logistic Regression
* Evaluation metrics and execution time

### Part B — Manual Implementation

Implemented using NumPy and Pandas:

* Missing-value handling
* Categorical encoding
* Feature scaling
* Linear Regression using least squares
* Logistic Regression using sigmoid and gradient descent
* Manual prediction and metric calculations

### Part C — Comparison and Optimization

* Comparison of Scikit-learn and manual implementations
* Optimization of manual Logistic Regression
* Evaluation of the optimized model
* Comparison of predictive performance and execution time

## Evaluation Metrics

### Regression

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Classification

* Accuracy
* Precision
* Recall
* F1-Score

Training time and prediction time are also recorded.

## Files

* `202618047_DS605_lab05.ipynb` — Main notebook
* `garments_worker_productivity.csv` — Dataset
* `regression_comparison.csv` — Regression comparison results
* `classification_comparison.csv` — Classification comparison results

## How to Run

1. Clone or download the repository.

2. Keep the notebook and dataset in the same folder.

3. Open the notebook in Jupyter Notebook or VS Code.

4. Install the required libraries by running the following command in the terminal:

   `pip install numpy pandas scikit-learn jupyter`

5. Run the notebook cells in order.

## Results and Observations

The notebook contains comparison tables for regression and classification models, including predictive metrics and execution times.

The optimized manual Logistic Regression model is also evaluated and compared with the other classification models.

Refer to the notebook outputs and generated CSV files for the measured results.

## Conclusion

This lab demonstrates how regression and classification workflows can be implemented using Scikit-learn and manually using NumPy and Pandas.

The comparison highlights differences in predictive performance, execution time, and implementation approaches.
