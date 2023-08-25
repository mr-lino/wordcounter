FROM python:3.10

WORKDIR /api

COPY . .

RUN pip install poetry

RUN poetry install

CMD [".venv/bin/uvicorn", "word_counter.main:app", "--host", "0.0.0.0", "--port", "8000"]