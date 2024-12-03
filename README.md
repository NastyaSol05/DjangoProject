# Django Project: Catalog Application

## Описание проекта
Проект создан для изучения основ Django. Включает приложение `catalog` с домашней страницей и страницей контактов. Стилизация выполнена с использованием Bootstrap. 

### Основные функции:
- Главная страница (home.html)
- Страница контактов (contacts.html)

## Установка и запуск проекта

### 1. Подготовка среды разработки
1. Создайте новую директорию для проекта:
   ```bash
   mkdir my_django_project
   cd my_django_project
2. Настройте виртуальное окружение:
  python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate     # для Windows

### 2. Инициализация Django-проекта
1. Установите Django:
   `pip install django`
2. Инициализируйте новый проект Django:
   `django-admin startproject my_project`
### Задание 1: Структура проекта
Создана структура проекта и настроен Git.

### Задание 2: Приложение catalog
1. Создайте приложение:
python manage.py startapp catalog

2. Зарегистрируйте приложение в my_project/settings.py:
INSTALLED_APPS = [..., 'catalog',]

3. Настройте маршрутизацию:
  Добавьте маршруты в catalog/urls.py.
  Подключите маршруты приложения в my_project/urls.py.
### Задание 3: Шаблоны
1. Создайте директорию для шаблонов:
  catalog/templates/catalog/
2. Добавьте файлы home.html и contacts.html.
  Для стилизации используйте Bootstrap.
### Задание 4: Контроллеры
1. Создайте контроллеры в catalog/views.py:
  from django.shortcuts import render
  def home(request):
      return render(request, 'catalog/home.html')

  def contacts(request):
      return render(request, 'catalog/contacts.html')
2. Настройте маршруты в catalog/urls.py:
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.home, name='home'),
      path('contacts/', views.contacts, name='contacts'),
  ]
### Запуск проекта
Примените миграции:
  python manage.py migrate
Запустите сервер разработки:
  python manage.py runserver
Откройте в браузере:
Главная страница: http://127.0.0.1:8000/
Страница контактов: http://127.0.0.1:8000/contacts/
### Рекомендации по разработке
Используйте Git для управления ветками.
Каждую задачу выполняйте в отдельной ветке.
Следуйте принципам чистого кода и DRY.


