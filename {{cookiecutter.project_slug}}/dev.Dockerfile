FROM python:{{cookiecutter.python_version}}-slim

WORKDIR /app
COPY . .

ARG VERSION=0.0.0
RUN sed -i "s/0\.0\.0/${VERSION:-0.0.0}/g" pyproject.toml
RUN sed -i "s/__VERSION__/${VERSION:-0.0.0}/g" ./version.py

ARG COMMIT=local
ENV COMMIT=${COMMIT}

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

WORKDIR /app/{{cookiecutter.project_slug}}/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]