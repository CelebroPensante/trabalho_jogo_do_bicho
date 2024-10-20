FROM python:3.9-slim
WORKDIR /extras
COPY automatic_wpp_analysis.py /extras
RUN pip install streamlit pandas plotly
EXPOSE 8501
CMD ["streamlit", "run", "automatic_wpp_analysis.py"]