import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core")
app.config_from_object("django.conf:settings",namespace="CELERY")

# app.conf.task_routes = {'cworker.tasks.task1':{'queue':'queue1'},
#                         'cworker.tasks.task2':{'queue':'queue2'},
#                         }

# tasks priority configs
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep':':',
    'queue_order_strategy':'priority',
}

app.autodiscover_tasks()