import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5566")

while True:
     message = socket.recv()
     print message
     socket.send("World")

