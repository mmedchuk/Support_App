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

## :gear: Application is powered by

**Core tools**

- ✔️ [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- ✔️ [Django 4.1](https://www.djangoproject.com/)

**Code quality tools**

- ✔️ [black](https://github.com/psf/black)
- ✔️ [flake8](https://github.com/pycqa/flake8)
- ✔️ [isort](https://github.com/PyCQA/isort)

</br>

## ⚠️ Mandatory steps

### 1. Clone the project from GITHub🌐

```bash
git clone https://github.com/mmedchuk/support_app
```

### 2. Setup and config environment 
<ul>
<li>Make sure if you have installed Python 3.10 interpreter.</li>
<li>Install Pipenv Enviroment and initialize it.</li>

```bash
#Install Pipenv
pip install pipenv

#Initialization
pipenv shell
```
<li>Install depencities from Lock file.</li>

```bash
pipenv sync
```
<li>Make sure all depencities are installed.</li>
<li>Install pre-commit hooks for code quality control before commit</li>

```bash
pre-commit install
```

</ul>

</br>

## 🏃 Start application
<p>To start this aplication you should to run it on local or remote server by command:</p>

```bash
#Port is optional. Default is 8000.
python manage.py runserver [port] 
```

## ⌛ Release History
<ul>
<li style="font-style: italic">1.0.0 Work in progress</li>
<p>- Initial app version</p>

</ul>

</br>

#### To be continued...