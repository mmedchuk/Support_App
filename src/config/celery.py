import os
from datetime import datetime
from time import sleep

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("config")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.task
def demo_task():

    sleep(5)
    print(f"Demo task was run at {datetime.now()}")
