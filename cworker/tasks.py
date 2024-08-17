from celery import shared_task

@shared_task
def task1():
    print('task1 is done successfully')

@shared_task
def task2():
    print('task2 is done successfully')