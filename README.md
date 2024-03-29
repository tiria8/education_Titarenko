## Описание

Небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули". В них есть:

- порядковый номер
- название
- описание
- владелец

### Используемый стэк
- python 3.11
- Docker
- Django==5.0.1
- djangorestframework 3.14.0
- PostgreSQL 16.1

## Проект

<aside>
При создании проекта:

1. Реализованы все методы CRUD для моделей Users и Modules.

2. Покрытие автоматизированными юнит-тестами составляет 95%.

</aside>

### Админка

Админ-панель доступна по адресу на локальном хосте http://127.0.0.1:8000/admin/ 

### Создание базы данных

Выполнить команду
```commandline
sudo -i -u postgres psql
```
После входа в postgres создаем БД
```commandline
CREATE DATABASE education;
```

### Интеграция с базой данных

В файле .env задать значения для параметров:

-POSTGRES_DB
-POSTGRES_USER
-POSTGRES_PASSWORD
-POSTGRES_HOST
-POSTGRES_PORT

После необходимо создать и применить миграции
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

### Запуск приложения на локальном хосте

Для запуска приложения на локальной машине нужно выполнить команду
```commandline
python manage.py runserver
```
Проект будет доступен по адресу:
http://127.0.0.1:8000/

### Создание суперпользователя

В файле .env задать значения для параметров:

-SUPER_USER_EMAIL
-SUPER_USER_PASSWORD

Выполнить команду
```commandline
python manage.py csu
```

Эти же значения нужно использовать для входа в админку

### Docker

Контейнеризация осуществлена на базе Docker, что позволяет упаковать приложение 
и все его зависимости в единый контейнер, который можно легко переносить 
и запускать на любой совместимой с Docker системе.

Запустить проект на докере команды в терминале.

**собрать проект**
```commandline
docker compose build
```

**запустить проект**
```commandline
docker-compose up
```

### Документация

Для проекта подготовлена документация на основе drf-yasg
Доступ к документации на локальном сервере по адресам:
http://127.0.0.1:8000/docs/ и http://127.0.0.1:8000/redoc/
