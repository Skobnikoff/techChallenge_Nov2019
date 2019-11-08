# import sys
import time
import zmq

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5556")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5557")

print("Waiting for work from master...")
while True:
    s = receiver.recv()

    # Simple progress indicator for the viewer
    print("Received request: %s" % str(s))

    # Do the work
    time.sleep(1)

    # Send results to sink
    sender.send_string('Processed task #{}'.format(str(s)))