FROM python:3.9.4-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app/movies
ENV PYTHONPATH /app/movies

CMD [ "python3", "main.py" ]
