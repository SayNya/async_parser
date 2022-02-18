FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN python -m pip install -U pip
RUN pip install poetry

WORKDIR /app

COPY system/* ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY src src/

RUN chmod +x entrypoint.sh
