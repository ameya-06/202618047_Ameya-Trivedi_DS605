# DS605 Lab 3 - Scikit-learn Data Preprocessing and Model Performance Evaluation

##Student Details 
Name: Ameya Trivedi
Student ID: 202618047

## Dataset

Kaggle Hotel Booking Demand dataset (`hotel_bookings.csv`).

## Objective

The objective of this assignment is to build and compare Scikit-learn preprocessing pipelines and evaluate Logistic Regression and Decision Tree classification models.

## Tasks Performed

### 1. Data Loading and Understanding

- Loaded the Hotel Booking Demand dataset using Pandas.
- Examined the dataset using:
  - `head()`
  - `shape`
  - `info()`
  - `describe()`
  - `dtypes`
- Used `is_canceled` as the target variable.
- Identified numerical and categorical features.

### 2. Missing Values, Leakage and Outliers

- Calculated missing-value count and percentage for every column.
- Identified columns with high missingness.
- Removed the `company` column because approximately 94% of its values were missing.
- Removed `reservation_status` and `reservation_status_date` to prevent data leakage.
- Checked numerical features for outliers using the IQR method.
- Removed only clear and extreme outliers.

### 3. Train-Test Split and Preprocessing

The data was split using:

- Test size: 20%
- Stratification: `y`
- Random state: 42

Two preprocessing pipelines were created:

**Pipeline A**
- KNNImputer
- StandardScaler

**Pipeline B**
- KNNImputer
- MinMaxScaler

For categorical features:
- SimpleImputer with `most_frequent`
- OneHotEncoder with `handle_unknown="ignore"`

ColumnTransformer and Pipeline were used to ensure preprocessing was fitted only on the training data.

### 4. Model Training

Four model-pipeline combinations were trained:

1. Logistic Regression + Pipeline A
2. Logistic Regression + Pipeline B
3. Decision Tree + Pipeline A
4. Decision Tree + Pipeline B

Model settings were kept unchanged across the comparison.

### 5. Model Evaluation

The models were evaluated using:

- Training Accuracy
- Testing Accuracy
- Precision
- Recall
- F1-Score

A final comparison table was created for all four experiments.

Confusion matrices were also plotted for:
- Best Logistic Regression model
- Best Decision Tree model

### 6. Observations

- Logistic Regression performance was compared using StandardScaler and MinMaxScaler.
- Decision Tree performance showed relatively little dependence on feature scaling.
- The model with the highest testing performance and F1-score was considered the best overall combination.
- The train-test accuracy difference was examined to identify possible overfitting.
- Confusion matrices were used to compare correct and incorrect classifications.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Repository Contents

- `202618047_DS605_Lab03.ipynb` - Assignment notebook
- `hotel_bookings.csv` - Dataset
- `README.md` - Project documentation