import streamlit as st

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model')

df = pd.read_csv('https://raw.githubusercontent.com/Ayu-Fitriani131/flu_vaccination/refs/heads/main/training_set_features.csv')
df
