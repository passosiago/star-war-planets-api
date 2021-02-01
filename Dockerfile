FROM python:3.8.5-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]