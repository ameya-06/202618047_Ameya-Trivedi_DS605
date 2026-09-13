import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path


# ---------------------------------------------------
# Load trained model
# ---------------------------------------------------
model_path = Path(__file__).parent / "airbnb_price_model_compressed.pkl"
model = joblib.load(model_path)


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Airbnb Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🏠 Airbnb Price Predictor")

st.write(
    "Enter the details of an Airbnb listing to estimate "
    "its price per night."
)


# ---------------------------------------------------
# User Inputs
# ---------------------------------------------------

st.subheader("Listing Details")


neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    [
        "Manhattan",
        "Brooklyn",
        "Queens",
        "Bronx",
        "Staten Island"
    ]
)


neighbourhood = st.text_input(
    "Neighbourhood",
    value="Midtown"
)


room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)


latitude = st.number_input(
    "Latitude",
    min_value=40.4,
    max_value=40.95,
    value=40.75,
    step=0.001
)


longitude = st.number_input(
    "Longitude",
    min_value=-74.3,
    max_value=-73.7,
    value=-73.98,
    step=0.001
)


minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    max_value=1250,
    value=3,
    step=1
)


number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    max_value=629,
    value=10,
    step=1
)


reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    max_value=58.5,
    value=1.0,
    step=0.1
)


host_listings_count = st.number_input(
    "Host Listings Count",
    min_value=1,
    max_value=327,
    value=1,
    step=1
)


availability_365 = st.number_input(
    "Availability (Days per Year)",
    min_value=0,
    max_value=365,
    value=100,
    step=1
)


# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if st.button("Predict Airbnb Price", type="primary"):

    # Apply the same log transformations used during training
    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "log_minimum_nights": [np.log1p(minimum_nights)],
        "log_number_of_reviews": [np.log1p(number_of_reviews)],
        "log_reviews_per_month": [np.log1p(reviews_per_month)],
        "log_host_listings_count": [np.log1p(host_listings_count)],
        "log_availability_365": [np.log1p(availability_365)]
    })

    # Predict log(price)
    prediction_log = model.predict(input_data)

    # Convert back to original price
    predicted_price = np.expm1(prediction_log)[0]

    # Display prediction
    st.success(
        f"Estimated Airbnb Price: ${predicted_price:,.2f} per night"
    )