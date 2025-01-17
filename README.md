# WhatsApp Data Analysis

Este projeto realiza a análise de dados de conversas do WhatsApp utilizando Streamlit, pandas e plotly.

## Estrutura do Projeto
/trabalho 4<br>
  └── app<br>
    ├── Dockerfile <br>
    ├── docker-compose.yml <br>
    ├── streamlit_data_show.py<br>
    └── data<br>
      ├── get_data.py <br>
      └── _chat.txt<br>
  └── extras<br>
    └── automatic_wpp_analysis.py<br>


## Pré-requisitos

- Docker
- Docker Compose

## Como Rodar a Aplicação

### Usando Docker

1. **Clone o repositório**:<br>
   `git clone https://github.com/CelebroPensante/trabalho_jogo_do_bicho`<br>
   `cd trabalho_jogo_do_bicho `
3. Construa a imagem e inicie o container:<br>
   `docker-compose up --build`
4. Acesse a aplicação:<br>
   `Abra o navegador e acesse http://localhost:8501.`

### Manualmente na Máquina
1. **Clone o repositório**:<br>
   `git clone https://github.com/CelebroPensante/trabalhojogo_do_bicho`<br>
   `cd trabalho_jogo_do_bicho`<br>
2.Crie um ambiente virtual e ative-o:<br>
  `python -m venv venv`<br>
  `venv\Scripts\activate`
3. Instale as dependências:<br>
  `pip install streamlit pandas plotly`
4. Execute a aplicação:<br>
  `streamlit run streamlit_data_show.py`
5. Acesse a aplicação:<br>
   `Abra o navegador e acesse http://localhost:8501.`

## Estrutura dos Arquivos
- 'Dockerfile: Define a imagem Docker para a aplicação.
- docker-compose.yml: Configura o serviço Docker para a aplicação.
- streamlit_data_show.py: Script principal que executa a aplicação Streamlit.
- data/get_data.py: Script que processa os dados do arquivo _chat.txt.

# Extra

Além do trabalho solicitado também há um arquivo extra q realiza a análise automatica para qualquer arquivo de dados do whatsapp

Para rodar ela é similar ao arquivo anterior.
![image](https://github.com/user-attachments/assets/e7dbc695-c257-4c8f-9f77-d935a4e6c061)

## Desenvolvedores:
- Vitor G. J. de Carvalho
- Lucas Tiepo
