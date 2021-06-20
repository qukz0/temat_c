import time
import zmq
import numpy as np
import pickle

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    n, m = np.random.randint(1,10,size=2)
    random_matrix = np.random.randint(1,10,size=(n,m))
   
    print(random_matrix)

    msg = pickle.dumps(random_matrix)
    socket.send(msg)
    message = socket.recv()
    time.sleep(1)

    print(pickle.loads(message))
