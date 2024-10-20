import streamlit as st
import pandas as pd
import plotly.express as px
import re

# titulo
st.title("automated whatsapp data analysis")
st.write("Desenvolvido por: Vitor g. j. de Carvalho e Lucas Tiepo")

# instruções
st.subheader("Como utilizar?")
st.write("1. Exporte a conversa do WhatsApp para um arquivo .txt:")
st.write("""
No Android\n
Abra o WhatsApp:
Inicie o aplicativo e vá até a conversa que deseja exportar.
Abra as Configurações da Conversa:
Toque nos três pontos no canto superior direito.
Selecione Mais e depois Exportar conversa.
Escolha Exportar sem Mídia:
Você terá a opção de exportar a conversa sem as mídias (fotos, vídeos, etc.).
Escolha o Método de Envio:
Selecione como deseja compartilhar a conversa exportada (por exemplo, por e-mail, Google Drive, etc.).
Envie o Arquivo:
Após escolher o método, o WhatsApp criará um arquivo .txt com a conversa e, se você escolher, anexará as mídias. Envie para você mesmo ou para outro contato.

No iPhone\n
Abra o WhatsApp:
Inicie o aplicativo e acesse a conversa que deseja exportar.
Abra as Configurações da Conversa:
Toque no nome do contato ou grupo na parte superior da tela.
Exportar Conversa:
Role para baixo e selecione Exportar Conversa.
Escolha Exportar sem Mídia:
exportar a conversa sem mídias.
Escolha o Método de Envio:
Selecione como deseja compartilhar a conversa exportada (por exemplo, por e-mail, iCloud, etc.).
Envie o Arquivo:
O WhatsApp criará um arquivo .txt e enviará as mídias, se selecionado, de acordo com sua escolha.
""")

st.write("2. Faça o upload do arquivo .txt exportado.")

# Upload de arquivo
file = st.file_uploader("Pick a file", type="txt")

if file is not None:
    # Carregar dados do arquivo
    data = file.read().decode('utf-8')
    
    # Ajustar as expressões regulares para capturar corretamente os dados
    pattern = r'\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] ([^:]+): (.*)'
    matches = re.findall(pattern, data)
    
    # Criar o DataFrame
    df = pd.DataFrame(matches, columns=['Date', 'Time', 'Name', 'Message'])

    # Preprocessamento do data
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

    df = df.sort_values(by='Name')  # Ordena por nome

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
else:
    st.write("Por favor, faça o upload de um arquivo para continuar.")