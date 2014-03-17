py-shm-manager
==============

Little python scripts showing the share of memory via a server.

The three scripts are in python 3.

The server create a empty queue and shared this one to clients.

One client is a productor and write numbers from 1 to 1337 inside the queue
(just an exemple of use). Then this client exit.

The second client is a consumer and try to read constantly into the queue. Then
it's just print the read numbers into stdin. This one continue to try to read
until an SIGINT is send (by ^C or kill).

Usage
-----

Start the server :

```
python server.py
```

Then start the consumer and productor :

```
python ./consumer.py &
python ./productor.py &
```

Many productor and consumer can be launched at the same time. For example :
```sh
python ./consumer.py &
for i in `seq 1 100`; python ./productor.py &; done
```
