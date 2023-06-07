# Сервис для сбора вопросов по викторинам

### Установка проекта

1. Скопируйте репозиторий

```
git clone https://github.com/VrHb/quiz-api-collector.git
```

2. Активируйте виртуальное окружение

```
python -m venv <название окружения>
```

3. Установите необходимые библиотеки

```
pip install -r requirements.txt
```

#### Переменные окружения

1. Создайте .env файл

```
touch .env
```

2. Добавьте пароль и порт для postgresql в файл

```
echo "PSQL_PASSWORD=<ваш пароль к бд>" >> .env";
echo "PSQL_PORT=<порт>" >> .env
```

#### Создание контейнера с postgresql

1. Запустите сборку контейнера

```
docker-compose up -d
```

### Запуск сервиса

```
uvicorn main:app --reload
```
