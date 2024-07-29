FROM python:3.12.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./ /app/
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "streamlit.py"]
