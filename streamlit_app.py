import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is app builds a machine learning model')

df = pd.read_csv('https://drive.google.com/drive/u/0/folders/16KqGaTACyiqZSn52qYlLIIJ8lpJTzeZP')
df
