import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de Dados de Veículos')

st.write('Dados dos veículos:')
st.dataframe(car_data)
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    # Adicione uma mensagem explicativa:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # IMPORTANTE: Atribua o resultado para a variável fig:
    fig = px.scatter(car_data, x='odometer', y='price')
    
    # Exiba o gráfico:
    st.plotly_chart(fig, use_container_width=True)
