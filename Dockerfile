# set base image
FROM python:3.8.2-slim

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy project code
COPY . /app/
