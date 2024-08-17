import os
from celery import Celery

app = Celery("sa-cworker")
app.config_from_object("celeryconfig")

@app.task
def add_numbers():
    return