FROM python:3.9.4-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH /app

CMD [ "python3", "./movies/main.py", "--host=0.0.0.0"]
