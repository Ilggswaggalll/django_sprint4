# Блогикум

Учебный Django-проект: публикации с изображениями, категории, профили пользователей, комментарии, пагинация и проверка прав автора.

## Запуск

Из корня репозитория:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py loaddata ../db.json
python manage.py createsuperuser
python manage.py runserver
```

Открыть http://127.0.0.1:8000/. Регистрация: `/auth/registration/`, админка: `/admin/`. Пароль администратора задаётся командой `createsuperuser`.

Письма восстановления пароля сохраняются локально в `blogicum/sent_emails/`. Изображения — в `blogicum/media/`. Эти каталоги и база SQLite не включаются в Git.

## Проверка

Из корня репозитория с активным окружением:

```bash
python -m pytest
python -m flake8 blogicum
```

Основа проекта и тесты: Яндекс Практикум, `yandex-praktikum/django_sprint4`. Выполненная предыдущая часть перенесена из `ap-django2`.
