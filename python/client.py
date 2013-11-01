import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5566")

socket.send("Hello")
message = socket.recv()
print repr(message)

