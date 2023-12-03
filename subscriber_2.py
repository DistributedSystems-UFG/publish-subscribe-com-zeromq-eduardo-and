import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "LIVETIME")  # subscribe to server LIVETIME messages


for i in range(100):  # Five iterations
	time = s.recv()   # receive a message
	print (bytes.decode(time))
                           