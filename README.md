# Сервис для сбора вопросов по викторинам

## Установка проекта

1. Скопируйте репозиторий

```
git clone https://github.com/VrHb/quiz-api-collector.git
```

2. Создайте .env файл

```
touch .env
```

3. Добавьте пароль для postgresql в файл

```
echo "PSQL_PASSWORD=<ваш пароль к бд>" >> .env
```


3. Запустите сборку контейнера

```sh
docker-compose build && docker-compose up -d
```

4. Убедитесь что контейнеры запустились

```sh
docker ps -a
```

## Пример запроса

```
curl -X 'POST' \
  'http://127.0.0.1:9000/quiz/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 3
}'
```
