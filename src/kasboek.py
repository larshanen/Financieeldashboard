import streamlit as st
import pandas as pd

st.title('Financieel dashboard')
st.subheader('Op basis van Rabobank categorieën')

df = st.file_uploader('Upload hier je kasboek (.xlsx):', type = 'xlsx')

if df is not None:
    df1 = pd.read_excel(df)
    st.dataframe(df1)