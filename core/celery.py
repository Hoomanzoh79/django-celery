import os
from celery import Celery

# celery configs
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core")
app.config_from_object("django.conf:settings",namespace="CELERY")

# task routing
# app.conf.task_routes = {'cworker.tasks.task1':{'queue':'queue1'},
#                         'cworker.tasks.task2':{'queue':'queue2'},
#                         }

# tasks priority configs
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep':':',
    'queue_order_strategy':'priority',
}

# tasks rate limit ---> the default value is 10/m 
# meaning 10 tasks per minute,we set it to 1 task per minute(of the same task)
app.conf.task_default_rate_limit = '1/m'

app.autodiscover_tasks()