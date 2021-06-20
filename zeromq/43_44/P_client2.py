import time
import zmq
import pickle

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

while True:
    socket.send(b"Hello")   
    time.sleep(1)
    message = socket.recv()
    print(f"Received reply request [{message}]")


