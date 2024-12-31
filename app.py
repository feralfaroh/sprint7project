import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv') 
df.info()

# Cleaning the data
df = df.dropna()
df['model_year'] = df['model_year'].astype(int)
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Titles
st.title('Vehicle Dataset')
st.write('Estudiante FERNANDO JESUS ALFARO HERNANDEZ')

# Show the data 
hist_button = st.button('Construir histograma')  # Crear un botón
        
if hist_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # Crear un histograma
    fig = px.histogram(df, x="odometer")
        
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    # Título
    st.write('Gráfico de barras')

    # Gráfico de barras
    gb = df.groupby(['model_year', 'fuel'])['odometer'].sum().reset_index()
    fig = px.bar(gb, x="model_year", y="odometer", color="fuel", barmode="stack")
    
    # Mostrar el gráfico de barras en la interfaz de Streamlit
    st.plotly_chart(fig, use_container_width=True)
