FROM python:3.11.9-slim

WORKDIR /app

# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get -y install gcc

# Устанавливаем Poetry и зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000 "]
