FROM python:3.9

RUN mkdir /Frontend

COPY requirements.txt /Frontend

WORKDIR /Frontend

RUN pip install -r requirements.txt

COPY . /Frontend

EXPOSE 2810