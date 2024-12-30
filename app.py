import streamlit as st
import pandas as pd
import plotly_express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')
# Titles
st.title('Vehicle dataset')
st.write('This is a simple example of a Streamlit app')
