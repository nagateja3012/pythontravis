FROM python:3.7-alphine


ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir/Laptop    
WORKDIR /Laptop
COPY ./Laptop /Laptop

RUN adduser -D user
USER user