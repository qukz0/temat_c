import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from server...")
socket.connect ("tcp://localhost:%s" % port)

topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

total_value = 0
for update_nbr in range (5):
    string = socket.recv_string()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print(topic, messagedata)
    
