import streamlit as st
import pandas as pd
import plotly.express as px
from data.get_data import get_data

# Load data
df = get_data()

# Preprocessamento do data
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

df = df.sort_values(by='Name') # Ordena por nome

# Sidebar
df['Name'] = df['Name'].apply(lambda x: str(x))
names_op = ["Todos"] + list(df["Name"].unique())
selected_names = st.sidebar.multiselect("Name", options=names_op, default="Todos")

# Filtrar dados
if "Todos" in selected_names:
    filtered_names = df["Name"].unique()
else:
    filtered_names = selected_names

df = df[df["Name"].isin(filtered_names)] 

# Filtrar dados a partir de outubro de 2024
start_date = pd.Timestamp('2024-10-01')
df = df[df['Date'] >= start_date]

# titulo
st.title("trabalho 4 - whatsapp data analysis")

st.write("Desenvolvido por: Vitor g. j. de Carvalho e Lucas Tiepo")

# Layout de duas colunas
col1, col2 = st.columns(2)

# Resumo da conversa
with col1:
    st.subheader("Resumo da conversa")
    st.write("Mensagens por participante: ", df["Name"].value_counts())

# Histórico do remetente
with col2:
    st.subheader("Histórico do remetente")
    st.write("Mensagens do remetente", df[["Name","Message", "Date", "Hour"]])

# Histograma da quantidade de conversas por dia para cada remetente
st.subheader("Histograma da quantidade de conversas por dia para cada remetente")
daily_messages = px.histogram(df, x='Date', color='Name', title='Quantidade de mensagens por dia para cada remetente')
st.plotly_chart(daily_messages)

# Gráfico de pizza: exibir um gráfico considerando o percentual de mensagens de cada remetente.
st.subheader("Gráfico de pizza")
msg_count = px.pie(df, names='Name', title='Percentual de mensagens de cada remetente')
st.plotly_chart(msg_count)

# Gráfico de linhas: apresentar a quantidade de mensagens ao longo do tempo (data) para cada remetente. 
st.subheader("Gráfico de linhas")
msg_count = df.groupby(['Date', 'Name']).size().reset_index(name='Message Count')
line_chart = px.line(msg_count, x='Date', y='Message Count', color='Name', title='Quantidade de mensagens ao longo do tempo para cada remetente')
st.plotly_chart(line_chart)

