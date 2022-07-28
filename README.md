### Описание проекта

Дынный проект написан в рамках выполнения итогового задания спирнта №15 в курсе Python-разработчик от Яндекс Практикума.
Проект решает задачу предоставления API интерфейса для работы с социальной сетью Yatube.
Через данный API интерфейс возможно создание сторонних приложений и WEB интерфейсов для данной соц. сети.

### Как запустить проект:

Для развертывания проекта должен быть установден Docker и Docker-Compose

Проверьте установлен ли у вас Docker
```
docker --version
Docker version 20.10.17, build 100c701
```
Если Docker не установлен, то установите по документации
https://docs.docker.com/engine/install/ubuntu/

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:pahan174/infra_sp2.git
```
```
cd infra_sp2/infra
```

Запустить Docker-Compose

```
docker-compose up -d --build
```
должны запустить 3 контейнера

```
Starting infra_db_1 ... done
Starting infra_web_1 ... done
Starting infra_nginx_1 ... done
```

Выполните по очереди команды:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```
## Проект готов к работе!!!

## Тестовые данные
С проектом поставляется тестовые данные для БД
Логин пароль администратора
```
pahan
12345678
```

Файл тестовых данных infra/fixtures.json

Если вы хотитете наполнить БД, то выполните следующие действия

Узнайте name контейнера infra_web
```
docker ps
```

Скопируйте файл fixtures.json в контейнер в директорию /app
```
sudo docker cp fixtures.json infra_web_1:/app
```
Зайти в bash нужного контейнера
```
docker exec -it <container_id> bash
```
Выполнить в открывшемся терминале:
```
python3 manage.py loaddata fixtures.json
```


### Пример наполнения .env файла.
Файл должен быть в директории /infra_sp2/infra

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

### Управление пользователями

Пользователяи создаются только из панели Администратора суперпользователя.
Создать суперпользховтеля через комсанду:

```
python3 manage.py createsuperusers
```

### Описание работы и примеры

После запуска сервера документация находится по адресу:

http://127.0.0.1:8000/redoc/

## Примеры запросов к API

Получить список всех публикаций:

```
GET-запрос
http://127.0.0.1:8000/api/v1/posts/
```

Создать публикацию:

```
POST-запрос
http://127.0.0.1:8000/api/v1/posts/
```

Создать комментарий к публикации с ID=1:

```
POST-запрос
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

## Получение JWT токенов

Работа с опасными методами API возможна только с помощью JWT токенов.

Получить JWT-токен

```
POST-запрос
http://127.0.0.1:8000/api/v1/jwt/create/
```
