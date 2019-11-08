import zmq
import time

# get input
# TODO

# init 0MQ context and define sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  send request to master
message = b"Hello"
print("Send request: %s" % message)
socket.send(message)

time.sleep(1)

#  wait for response from master
response = socket.recv()
print("Received response: %s" % response)