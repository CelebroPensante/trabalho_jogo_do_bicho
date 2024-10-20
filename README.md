# WhatsApp Data Analysis

Este projeto realiza a análise de dados de conversas do WhatsApp utilizando Streamlit, pandas e plotly.

## Estrutura do Projeto
/trabalho 4
  └── app
    ├── Dockerfile 
    ├── docker-compose.yml 
    ├── streamlit_data_show.py
    └── data
      ├── get_data.py 
      └── _chat.txt
  └── extras
    └── automatic_wpp_analysis.py


## Pré-requisitos

- Docker
- Docker Compose

## Como Rodar a Aplicação

### Usando Docker

1. **Clone o repositório**:
   git clone https://github.com/CelebroPensante/trabalho_jogo_do_bicho
   cd trabalho_jogo_do_bicho  
2. Construa a imagem e inicie o container:
   docker-compose up --build
3. Acesse a aplicação: 
   Abra o navegador e acesse http://localhost:8501.

### Manualmente na Máquina
1. **Clone o repositório**:
   git clone https://github.com/CelebroPensante/trabalhojogo_do_bicho
   cd trabalho_jogo_do_bicho
2.Crie um ambiente virtual e ative-o:
  python -m venv venv
  venv\Scripts\activate
3. Instale as dependências:
  pip install streamlit pandas plotly
4. Execute a aplicação:
  streamlit run streamlit_data_show.py
5. Acesse a aplicação:
   Abra o navegador e acesse http://localhost:8501.

##Estrutura dos Arquivos
- 'Dockerfile: Define a imagem Docker para a aplicação.
- docker-compose.yml: Configura o serviço Docker para a aplicação.
- streamlit_data_show.py: Script principal que executa a aplicação Streamlit.
- data/get_data.py: Script que processa os dados do arquivo _chat.txt.

##Desenvolvedores:
- Vitor G. J. de Carvalho
- Lucas Tiepo
