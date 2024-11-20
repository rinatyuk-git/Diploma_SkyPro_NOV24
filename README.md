# Сервис обработки загружаемых документов
![Python](https://img.shields.io/badge/Python-3.11.9-blue)
![Django](https://img.shields.io/badge/django-5.1.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/django--rest--framework-3.15.2-blue?labelColor=333333&logo=django&logoColor=white&color=blue)
![DRF-simpleJWT](https://img.shields.io/badge/django--rest--framework--simplejwt-5.3.1-blue?labelColor=333333&logo=django&logoColor=white&color=blue)
![Celery](https://img.shields.io/badge/Celery-5.4.0-&logo=Celery&logoColor=FFFFFF&label)
![Redis](https://img.shields.io/badge/Redis-5.2.0-DC382D?&logo=redis&logoColor=white)


## Описание основных моментов проекта:

- Необходимо создать сервис для обработки загружаемых документов.
- Сервис должен позволять зарегистрированным пользователям загружать документы через API.
- При загрузке документа администратор платформы - Moderator, должен получать уведомление по электронной почте.
- Moderator может просматривать, подтверждать или отклонять загруженные документы через Django admin.
- После подтверждения или отклонения документа пользователю, загрузившему документ, должно приходить уведомление по электронной почте.
- Для обработки уведомлений необходимо использовать систему очередей.


## Задачи проекта

1. Создать API для загрузки документов зарегистрированными пользователями.
2. Настроить уведомление администратора по электронной почте при загрузке нового документа.
3. Добавить в Django admin быстрые действия для подтверждения или отклонения загруженных документов.
4. Настроить отправку уведомлений по электронной почте пользователю, когда его документ подтвержден или отклонен.
5. Реализовать систему очередей для отправки уведомлений.


## Структура проекта
```bash
Diploma_SkyPro_NOV24
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── content
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_document_is_approved.py
│   │   ├── 0003_remove_document_is_approved_document_status.py
│   │   ├── 0004_alter_document_options.py
│   │   ├── 0005_alter_document_name.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users
│   ├── management
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── cmu.py
│   │   │   ├── csu.py
│   │   │   └── fillusers.py
│   │   └── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .coverage
├── .dockerignore
├── .env.sample
├── .flake8
├── .gitignore
├── Dockerfile
├── README.md
├── content.json
├── docker-compose.yaml
├── groups.json
├── manage.py
├── poetry.lock
├── pyproject.toml
└── users.json
```

## Документация
Документация по использованию API будет доступна после запуска сервера по ссылке: http://0.0.0.0:9000/swagger/

## Запуск данного проекта:

- Установите Git и Docker

- Клонируйте репозиторий 
```bash
git clone git@github.com:rinatyuk-git/Diploma_SkyPro_NOV24.git
```

- В виртуальном окружении установите пакет с зависимостями pyproject.toml
```bash
poetry shell
poetry install
```

- Добавьте в свой проект файл .env с необходимыми для работы переменными окружения. Образец .env.sample размещен в структуре проекта.

- Запустите терминал и выполните команды:
```bash
docker-compose up -d --build    
```

## Технические требования:

✔Фреймворк: Использовать фреймворк Django и Django Rest Framework (DRF) для реализации проекта.

✔База данных: Использовать PostgreSQL для хранения данных.

✔Контейнеризация: Использовать Docker и Docker compose для контейнеризации приложения.

✔Очередь сообщений:
Использовать Celery или другую систему очередей для отправки уведомлений.

✔Отправка уведомлений:
Настроить отправку уведомлений по электронной почте с использованием Django.

✔Документация: В корне проекта должен быть файл README.md с описанием структуры проекта и инструкциями по установке и запуску.

✔Реализовать автогенерируемую документацию API с использованием Swagger.

✔Качество кода: Соблюдать стандарты PEP8.

✔Весь код должен храниться в удаленном Git репозитории.

✔Тестирование: Код должен быть покрыт тестами с покрытием не менее 75%.
