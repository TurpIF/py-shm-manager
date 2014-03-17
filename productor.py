from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue')

HOST = '127.0.0.1'
PORT = 4242
KEY = bytes('my-key', 'ascii')
manager = QueueManager((HOST, PORT), authkey=KEY)
manager.connect()

queue = manager.get_queue()
for i in range(1337):
    print('Envoie :', i)
    queue.put(i)
