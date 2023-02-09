import streamlit as st
import pandas as pd
import base64

def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # encode the data into base64 format
    href = f'<a href="data:file/csv;base64,{b64}" download="download.csv">Download CSV File</a>'
    return href

st.title("Application de test")
st.write("Ceci est une application web pour apprendre à utiliser Streamlit")

uploaded_file = st.file_uploader("Upload a CSV file", type = "csv")
if uploaded_file is not None :
    df = pd.read_csv(uploaded_file, sep = ";")
    df["col3"] = df["col1"] + df["col2"]
    if st.button("Download processed CSV file") :
        st.markdown(download_csv(df), unsafe_allow_html=True)

