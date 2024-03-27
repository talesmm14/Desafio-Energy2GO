FROM python:3-alpine
LABEL authors="talesmelquiades : talesmelquiades@hotmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR app

RUN apk update

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

COPY . .

EXPOSE 8000
