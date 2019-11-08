import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  wait for client request
    message = socket.recv()
    print("Received request: %s" % message)

    #  partition work
    # TODO

    # send tasks to slaves
    # TODO

    # wait for responses from slaves
    # TODO

    # assemble results
    # TODO

    time.sleep(1)

    #  send reply back to client
    response = b"World"
    print("Send response: %s" % response)
    socket.send(response)
