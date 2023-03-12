run: 
	python src/manage.py runserver

cqch:
	black . && isort . && flake8 . && mypy .

celery:
	celery -A config worker -l INFO