import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model')

df = pd.read_csv('https://www.kaggle.com/datasets/darkknight98/flu-shot-prediction')
df
