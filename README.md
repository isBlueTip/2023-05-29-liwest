# Liwest

## Описание проекта

CRUD API товарных категорий, групп и самих товаров

## Установка проекта локально

В папке склонированного репозитория выполните:

```bash
docker-compose up --build
```
в соседнем терминале:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Стек

Django, Django REST framework, Docker-compose

## Автор

Семён Егоров  

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)
