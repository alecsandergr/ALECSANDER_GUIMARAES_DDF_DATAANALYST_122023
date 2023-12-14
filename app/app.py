import pandas as pd
import streamlit as st

from data_analysis import data_analysis_page
from generator import generate_presentation
from prediction import prediction_page

# Loading your DataFrame
df = pd.read_json("./data/bronze/product_features.json")

# Set the title for your Streamlit app page
st.title("Product Information App")

# Create a navigation sidebar
st.sidebar.title("Choose the Page")
page = st.sidebar.radio("Navigation", ["Data Analysis", "Prediction", "Presentation"])

# Depending on the selected page, call the corresponding function
if page == "Data Analysis":
    data_analysis_page(df)
elif page == "Prediction":
    prediction_page(df)
elif page == "Presentation":
    generate_presentation(df)
