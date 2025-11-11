import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Graph", layout="wide")

if "traces" not in st.session_state:
    st.session_state["traces"] = []

st.title("První divný graf")

uploaded_file = st.file_uploader("Upload a csv file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep = ",")
    st.dataframe(df)
    st.subheader("add date to the plot")
    col1, col2 = st.columns(2)
    with col1:
      x_column = st.selectbox("Select x-axis column", df.columns)
    with col2:
      y_column = st.selectbox("Select y-axis column", df.columns)
    col3, col4, col5 = st.columns(3)
    with col3:
      x_label = st.text_input("Name of the x-axis label", value=x_column)
      y_label = st.text_input("Name of the y-axis label", value=x_column)
