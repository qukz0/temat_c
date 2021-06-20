import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5559")

while True:
    socket.send_string("Server message to client")
    msg = socket.recv_string()
    print(msg)
    time.sleep(1)

