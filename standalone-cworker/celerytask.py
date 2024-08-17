import os
from celery import Celery

app = Celery("sa-cworker")
app.config_from_object("celeryconfig")
app.conf.imports = ('tasks')
app.autodiscover_tasks()