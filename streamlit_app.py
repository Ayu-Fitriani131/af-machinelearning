import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model')

# Corrected Google Drive link
csv_url = 'https://drive.google.com/drive/u/0/folders/16KqGaTACyiqZSn52qYlLIIJ8lpJTzeZP'  # Replace FILE_ID with the actual file ID
try:
    df = pd.read_csv(csv_url)
    st.dataframe(df)
except Exception as e:
    st.error(f"Error loading data: {e}")
