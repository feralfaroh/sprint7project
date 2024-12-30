import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
df

st.title('Vehicle dataset')
st.write('This is a simple example of a Streamlit app')
