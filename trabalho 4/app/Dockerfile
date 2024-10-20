FROM python:3.9-slim
WORKDIR /app
COPY streamlit_data_show.py /app
COPY data /app/data
RUN pip install streamlit pandas plotly
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_data_show.py"]