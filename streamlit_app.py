import pandas as pd
import numpy as np
import streamlit as st
#====================================Codigo Principal==================================================
uploaded_file = st.file_uploader("Carregue o Arquivo!")
if uploaded_file is not None:
    dataframe = pd.read_csv(r"C:\Users\Lucas\Desktop\Relatorio.csv",encoding="ISO-8859-1", sep = ';')
    st.write(dataframe)
