import time
import zmq
import pickle
from random import randint, random

context = zmq.Context.instance()
socket = context.socket(zmq.DEALER)
identity = u'Worker-%d' % randint(0,1000)
socket.identity = identity.encode('ascii')
socket.connect("tcp://localhost:5559")
print('Client %s started' % (identity))
reqs = 0
while True:
    reqs = reqs + 1
    print('Req #%d sent...' % (reqs))
    socket.send_string(u'request #%d' % (reqs))
    for _ in range(5):
        message = socket.recv()
        print('Client %s received: %s' % (identity, message))


