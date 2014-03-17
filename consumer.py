from multiprocessing.managers import BaseManager

# Indicate to the custom BaseManager class to get the *get_queue* operation
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')

# Connect to the server
HOST = '127.0.0.1'
PORT = 4242
KEY = bytes('my-key', 'ascii')
manager = QueueManager((HOST, PORT), authkey=KEY)
manager.connect()

# Get the shared queue
queue = manager.get_queue()

# Read while not SIGINT
try:
    while True:
        # Read value from the queue
        value = queue.get()
        print('Réception :', value)
except KeyboardInterrupt:
    pass
