from celery import shared_task
import time

@shared_task
def task1(queue='celery'):
    time.sleep(3)
    print('task1 is done successfully')

@shared_task
def task2(queue='celery:1'):
    time.sleep(3)
    print('task2 is done successfully')

@shared_task
def task3(queue='celery:2'):
    time.sleep(3)
    print('task3 is done successfully')

@shared_task
def task4(queue='celery:3'):
    time.sleep(3)
    print('task4 is done successfully')