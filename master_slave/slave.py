import os
import time
import zmq

SLAVE_ID = os.getpid()

if __name__ == '__main__':

    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5556")

    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5557")

    print("SLAVE {}: Waiting for work from Master...".format(SLAVE_ID))
    while True:
        task = receiver.recv_json()

        print("SLAVE {}: Received a task from Master: {}".format(SLAVE_ID, task["task_id"]))

        # multiply vectors
        matrix_1, matrix_2 = task["data"][0], task["data"][1]
        message_to_master = {
            "task_id": task["task_id"],
            "slave_id": SLAVE_ID,
            "result": sum(map(lambda x: x[0]*x[1], zip(matrix_1, matrix_2)))
        }
        time.sleep(1)

        # Send results to master
        sender.send_json(message_to_master)
        print("SLAVE {}: Sent result to Master: {}".format(SLAVE_ID, task["task_id"]))
