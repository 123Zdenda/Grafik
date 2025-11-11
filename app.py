import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Graph", layout="wide")

if "traces" not in st.session_state:
    st.session_state["traces"] = []

st.title("První divný graf")
