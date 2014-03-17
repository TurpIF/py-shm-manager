from multiprocessing.managers import BaseManager
from multiprocessing import Queue

queue = Queue()

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue', lambda: queue)

PORT = 4242
KEY = bytes('my-key', 'ascii')
manager = QueueManager('/tmp/coucou', authkey=KEY)
manager.get_server().serve_forever()
