FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы pyproject.toml и poetry.lock (если есть)
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем исходный код проекта в контейнер
COPY src/ ./src/

# Команда для запуска бота
CMD ["poetry", "run", "python", "src/main.py"]