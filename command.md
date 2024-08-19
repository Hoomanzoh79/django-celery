<!-- tasks grouping -->

from celery import group
from cworker.tasks import task1,task2,task3,task4
task_group = group(task1.s(),task2.s(),task3.s(),task4.s())
task_group.apply_async()

<!-- tasks chaining : tasks are processed sequentially and one after another with pre-defined order
tasks grouping : tasks are processed imparallel without any order -->

task_chain = chain(task1.s(5),task2.s(),task3.s())
task_chain.apply_async()
