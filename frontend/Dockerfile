FROM python:3.9

WORKDIR /app

RUN apt-get update

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]