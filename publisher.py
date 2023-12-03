from datetime import datetime
import zmq, time
from constPS import *  # -

context = zmq.Context()
s = context.socket(zmq.PUB)  # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT # how and where to communicate
s.bind(p)  # bind socket to the address
startTime = datetime.now()
staticMsg = "Hi! I'm static"

while True:
    time.sleep(5)  # wait every 5 seconds
    msgTime = str.encode("TIME " + time.asctime())
    timeDif = datetime.now() - startTime
    msgLiveTime = str.encode("LIVETIME " + str(timeDif.seconds)+" seconds")
    msgStaticEncoded = str.encode("STATIC " + staticMsg)

    s.send(msgTime)  # publish the current time
    s.send(msgLiveTime)  # publish server live time
    s.send(msgStaticEncoded)  # publish static msg
