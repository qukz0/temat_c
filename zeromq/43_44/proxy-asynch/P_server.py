import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    ident, message = socket.recv_multipart()
    print('Server received %s from %s' % (message, ident))
    replies = randint(0,4)
    for _ in range(replies):
        time.sleep(1. / (randint(1,10)))
        socket.send_multipart([ident, message])
