import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model')

# Corrected Google Drive link
csv_url = 'https://drive.google.com/uc?id=training_set_features.csv'  # Replace FILE_ID with the actual file ID
try:
    df = pd.read_csv(csv_url)
    st.dataframe(df)
except Exception as e:
    st.error(f"Error loading data: {e}")
