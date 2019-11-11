import time
import zmq


if __name__ == '__main__':

    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5556")

    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5557")

    while True:
        print("Waiting for work from master...")
        task = receiver.recv_json()

        print("Received request: {}".format(task["task_id"]))

        # multiply vectors
        matrix_1, matrix_2 = task["data"][0], task["data"][1]
        message_to_master = {
            "task_id": task["task_id"],
            "result": sum(map(lambda x: x[0]*x[1], zip(matrix_1, matrix_2)))
        }
        time.sleep(1)

        # Send results to master
        print("Send response to master: {}".format(task["task_id"]))
        sender.send_json(message_to_master)