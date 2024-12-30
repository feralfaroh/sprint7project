import streamlit as st
import pandas as pd
import plotly_express as px

# Load the data
df = pd.read_csv('vehicles_us.csv') 
df.info()

#Cleaning the data
df = df.dropna()
df['model_year'] = df['model_year'].astype(int)
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Titles
st.title('Vehicle dataset')
st.write('Estudiante FERNANDO JESUS ALFARO HERNANDEZ')

# Show the data
df
