"""Napisati program koji predstavlja raspoređivač (en. scheduler) zadataka koji
distribuira listu zadataka ka više radnih niti (en. worker threads) koristeći red (en.
queue). Svaka radna nit treba da preuzima zadatke iz reda i da ih obrađuje."""

import threading
import queue
import time

tasks = [1,2,3,4,5,6,7,8,9,10]

def process_task(task_id):
    print(f"Start processing task {task_id} in worker thread {threading.current_thread().name}")
    time.sleep(2)
    print(f"End processing task {task_id} in worker thread {threading.current_thread().name}")

def distribute_task(tasks_queue):
    while True:
        try:
            processing_task = tasks_queue.get(timeout = 1)
            process_task(processing_task)
            tasks_queue.task_done()
        except queue.Empty:
            break

tasks_queue = queue.Queue()
workers = []

for t in tasks:
    tasks_queue.put(t)

for i in range(1, 4):
    worker = threading.Thread(target = distribute_task, args=(tasks_queue,), name=f'worker {i}')
    worker.start()
    workers.append(worker)

for worker in workers:
    worker.join()

print('all tasks done')