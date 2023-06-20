FROM python:3.11-alpine3.18

RUN pip install poetry==1.4.0

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app/
