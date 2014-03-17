from multiprocessing.managers import BaseManager
from multiprocessing import Queue

# Creation of the used queue
queue = Queue()

# Customize the BaseManager class by registering a new operation
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', lambda: queue)

# Start the server
PORT = 4242
KEY = bytes('my-key', 'ascii')
manager = QueueManager(('', PORT), authkey=KEY)
manager.get_server().serve_forever()
