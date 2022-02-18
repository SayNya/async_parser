FROM python:3.10

RUN pip3 install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY src src/

CMD uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
