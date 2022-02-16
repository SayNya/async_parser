FROM python:3.10

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

WORKDIR /app

COPY pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY src src/

CMD uvicorn src.api.main:app --reload --workers 1 --host 127.0.0.1 --port 8000
