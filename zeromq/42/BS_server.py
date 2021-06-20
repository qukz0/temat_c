import time
import zmq
import pickle
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    
    x = pickle.loads(message)
    
    final = x * 2
    
    print(final)

    time.sleep(1)
    message = pickle.dumps(final)

    socket.send(message)
