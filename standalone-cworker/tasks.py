from celery import shared_task

@shared_task
def task3():
    print('task3 is done successfully (standalone worker)')

@shared_task
def task4():
    print('task4 is done successfully (standalone worker)')