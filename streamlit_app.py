import pandas as pd
import numpy as np
import streamlit as st
#====================================Codigo Principal==================================================
uploaded_file = st.file_uploader("Carregue o Arquivo!")

if uploaded_file is not None:
    for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
