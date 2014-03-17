from multiprocessing.managers import BaseManager
from queue import Empty

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue')

HOST = '127.0.0.1'
PORT = 4242
KEY = bytes('my-key', 'ascii')
manager = QueueManager((HOST, PORT), authkey=KEY)
manager.connect()

queue = manager.get_queue()
try:
    while True:
        try:
            value = queue.get_nowait()
        except Empty:
            break
        print('Réception :', value)
except KeyboardInterrupt:
    pass
