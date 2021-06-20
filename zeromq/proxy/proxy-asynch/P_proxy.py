import time
import zmq
import pickle

context = zmq.Context()
router = context.socket(zmq.ROUTER)
dealer = context.socket(zmq.DEALER)
router.bind("tcp://*:5559")
dealer.bind("tcp://*:5560")

poller = zmq.Poller()
poller.register(router, zmq.POLLIN)
poller.register(dealer, zmq.POLLIN)

while True:
    socks = dict(poller.poll())

    if socks.get(router) == zmq.POLLIN:
        ident, msg = router.recv_multipart()
        dealer.send_multipart([ident, msg])

    if socks.get(dealer) == zmq.POLLIN:
        ident, msg = dealer.recv_multipart()
        router.send_multipart([ident, msg])

