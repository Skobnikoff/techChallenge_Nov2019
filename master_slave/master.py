import time
import zmq

context = zmq.Context()

# socket communicating with clients
server = context.socket(zmq.REP)
server.bind("tcp://*:5555")

# socket pushing work to slaves
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5556")

# socket receiving results from slaves
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5557")

print("Waiting for a request from client...")
while True:
    #  wait for client request
    message = server.recv()
    print("Received request: %s" % message)

    #  partition work
    # TODO

    # send tasks to slaves
    for i in range(5):
        print("Send to slave task #{}".format(str(i)))
        sender.send_string(u"Task from master #{}".format(str(i)))

    # wait for responses from slaves
    for i in range(5):
        slave_response = receiver.recv_string()
        print("Response from slave: {}".format(slave_response))
    # assemble results
    # TODO

    time.sleep(1)

    #  send reply back to client
    response = b"World"
    print("Send response to client: %s" % response)
    server.send(response)
