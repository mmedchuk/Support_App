# README

# Support App

<a href="https://www.python.org/downloads/release/python-3100/">
    <img src="https://img.shields.io/badge/python_versions-3.10+-blue.svg">
</a>
<a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/django-4.1.0-blue">
</a>
<a img src="https://img.shields.io/badge/django-4.1.0-blue/">
</a>

![Build Status](https://github.com/mmedchuk/support_app/actions/workflows/code_quality.yml/badge.svg?branch=main)
</br>

<p align="left"><span style="font-style: italic; font-weight: bold">Support app</span> is an application created to help in communication with customers to solve issues. It`s suitable for projects were communication app between users is needed like web services, marketplaces, online shops, etc... </p>
</br>

## Application is powered by

**Core tools**

- ✔️ [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- ✔️ [Django 4.1](https://www.djangoproject.com/)

**Code quality tools**

- ✔️ [black](https://github.com/psf/black)
- ✔️ [flake8](https://github.com/pycqa/flake8)
- ✔️ [isort](https://github.com/PyCQA/isort)
- ✔️ [mypy](https://github.com/python/mypy)

**Additional tools**
- ✔️ [Docker](https://www.docker.com)
- ✔️ [Gunicorn](https://gunicorn.org/)

</br>

## ⚠️ Mandatory steps

### 1. Clone the project from GITHub🌐

```bash
git clone https://github.com/mmedchuk/support_app
```

### 2. Setup and config environment

- Make sure if you have installed Python 3.10 interpreter.
- Install Pipenv Enviroment and initialize it.

```bash
#Install Pipenv
pip install pipenv

#Initialization of virtual enviroment
pipenv shell
```

- Install depencities from Lock file.

```bash
pipenv sync
```

- Make sure all depencities are installed.
- Install pre-commit hooks for code quality control before commit

```bash
pre-commit install
```
<br>

## 🏃 Quickstart


We tried to make getting started with our app quick and painless. To start quick use we implement Docker technology which takes care of most of the installation process for this API. 
To start installation run the following steps:
<ol>
<li>Make sure you have installed Python
<li>Install an appopriate Docker version
<li> Run Docker-compose command to start installation

```bash
# Build images
docker-compose build

# Build image from scratch witout cache
docker-compose build --no-cache
```
<li> Wait a few time when Docker when install ang configure all tools
<li> After installation you can use our API

</ol>

</br>

##  ➕ Some usefull Docker-compose commands


```bash
# Run container
docker-compose up -d

# Build images
docker-compose build

# Stop containers
docker-compose down

# Restart containers
docker-compose restart

# Check containers status
docker-compose ps

## Logs

# get all logs
docker-compose logs

# get specific logs
docker-compose logs app

# get limited logs
docker-compose logs --tail 10 app

# get flowed logs
docker-compose logs -f app
```

</br>

## Additional information

### Usefull commands:

```bash
# Run project with Gunicorn server
gunicorn src.config.wsgi:application --localhost:8000

# Run project with Gunicorn server configused in the separate conf.file
gunicorn src.config.wsgi:application -c gunicorn.conf.py

```

### Application description:

```
▾ users
    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ views.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    ├─ admin.py # Database tables mapper
    └─ views.py # Endopints / post-controller
```

**Database:**

```mermaid
API DB Schema
erDiagram

    Users {
        int id
        string frist_name
        string last_name
        string email
        string password
        bool is_staff
        bool is_active
        string role
        datetime created_at
        datetime updated_at
    }
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        text body
        datetime created_at
        datetime updated_at
    }
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        text body
        datetime created_at
        datetime updated_at
    }

    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""
```

## ⌛ Release History

*1.0.0 Work in progress*

- Initial app version

### To be continued…
