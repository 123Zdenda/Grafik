import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Graph", layout="wide")

if "traces" not in st.session_state:
    st.session_state["traces"] = []

st.title("První divný graf")

uploaded_file = st.file_uploader("Upload a csv file")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep = ",")
        st.dataframe(df)
    st.subheader("add date to the plot")
    col1, col2 = st.columns(2)
      with col1:
        x_column = st.selectbox("Select x-axis column", df.columns)
      with col2:
        

    except Exception as  e:
        st.error(f"toto je chyba {e}")
