# import sys
import time
import zmq


if __name__ == '__main__':

    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5556")

    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5557")

    while True:
        print("Waiting for work from master...")
        task = receiver.recv_json()

        print("Received request: %s" % task)

        # Do the work
        task["result"] = "good"
        time.sleep(1)

        # Send results to sink
        print("Send response to master: %s" % task)
        sender.send_json(task)