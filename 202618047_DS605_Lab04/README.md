# Airbnb Price Prediction – DS605 Lab 04

## Project Overview

This project implements an end-to-end Machine Learning workflow for predicting the nightly price of Airbnb listings in New York City using the New York City Airbnb Open Data (2019) dataset.

The project covers data analysis and preparation, regression model training and evaluation, hyperparameter tuning, and deployment of the final model through a Streamlit web application.

## Task 1 – Data Analysis and Preparation

- Loaded and analyzed the Airbnb NYC 2019 dataset.
- Handled missing values and duplicate records.
- Removed invalid zero-price listings.
- Investigated price distributions and potential outliers.
- Performed exploratory data analysis using room type, neighbourhood group, location, minimum nights, reviews, and availability.
- Applied log transformation to skewed numerical features.
- Selected the following features for modelling:
  - `neighbourhood_group`
  - `neighbourhood`
  - `latitude`
  - `longitude`
  - `room_type`
  - `log_minimum_nights`
  - `log_number_of_reviews`
  - `log_reviews_per_month`
  - `log_host_listings_count`
  - `log_availability_365`
- Used `log1p(price)` as the transformed target for model training.

## Task 2 – Model Training and Evaluation

Three regression approaches were compared:

- Linear Regression
- Random Forest Regression
- Gradient Boosting Regression

The final selected model was **Random Forest Regression with a log-transformed target**.

### Final Model Performance

| Metric | Test Performance |
|---|---:|
| MAE | 56.32 |
| RMSE | 175.14 |
| R² | 0.234 |

Hyperparameter tuning was performed using GridSearchCV. Although the tuned model slightly improved MAE, the baseline Random Forest with the log-transformed target provided better overall RMSE and R², so it was retained as the final model.

## Task 3 – Streamlit Application

A Streamlit application was developed to allow users to enter Airbnb listing information and receive an estimated nightly price.

### Application Inputs

- Neighbourhood Group
- Neighbourhood
- Room Type
- Latitude
- Longitude
- Minimum Nights
- Number of Reviews
- Reviews per Month
- Host Listings Count
- Availability in 365 Days

The application applies the same feature transformations used during model training and returns the predicted nightly price in US dollars.

### Live Application

**Streamlit App:** https://airbnb-price-predictor-ameya.streamlit.app/

### Example Test

A realistic Manhattan/Midtown listing was tested with the deployed application, producing an estimated nightly price of **$226.06 per night**.

## Task 4 – Final Project Summary

The complete project documentation is provided in:

**`Task4 - Final Project Summary.pdf`**

The documentation contains the analysis summary, model comparison, final performance, application results, limitations, and conclusion.

## Project Files

| File | Description |
|---|---|
| `202618047_DS605_lab04.ipynb` | Complete ML analysis, preprocessing, model training and evaluation |
| `AB_NYC_2019.csv` | New York City Airbnb 2019 dataset |
| `app.py` | Streamlit application |
| `requirements.txt` | Python dependencies required to run the application |
| `airbnb_price_model_compressed.pkl` | Saved trained preprocessing and Random Forest model |
| `New_York_City_.png` | Project/location image |
| `Task4 - Final Project Summary.pdf` | Final project documentation |
| `README.md` | Project overview and usage instructions |

## How to Run the Application Locally

1. Clone or download this repository.
2. Open a terminal inside the `202618047_DS605_Lab04` folder.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

5. Open the local Streamlit URL shown in the terminal.

## Conclusion

The project demonstrates a complete machine-learning pipeline from raw Airbnb data analysis and preprocessing to model evaluation and deployment. The final Random Forest model with a log-transformed target was selected based on the overall comparison, and the trained model was integrated into a working Streamlit application.
