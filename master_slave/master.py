import time
import zmq


def partition_work(matrix_1, matrix_2):
    tasks = {}
    for row_index, row_matrix_1 in enumerate(matrix_1):
        for col_index, col_matrix_2 in enumerate(matrix_2):
            task = {"data": (row_matrix_1, col_matrix_2), "indexes": (row_index, col_index), "status": "todo"}
            tasks['{}_{}'.format(*task["indexes"])] = task
    return tasks


if __name__ == '__main__':

    context = zmq.Context()

    # socket communicating with clients
    server = context.socket(zmq.REP)
    server.bind("tcp://*:5555")

    # socket pushing work to slaves
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5556")

    # socket receiving results from slaves
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5557")

    while True:
        #  wait for client request
        print("Waiting for a request from client...")

        client_input_data = server.recv_json()
        print("Received request: %s" % client_input_data)

        #  partition work
        tasks = partition_work(client_input_data["matrix_1"], client_input_data["matrix_2"])

        # send tasks to slaves
        for task_id, task in tasks.items():
            print("Send to slave task: {}".format(task_id))
            sender.send_json(task)
            task['status'] = 'sent'

        # wait for responses from slaves
        for index in range(len(tasks.keys())):
            slave_response = receiver.recv_json()
            print("Response from slave: {}".format(slave_response))

        # assemble results
        # TODO

        time.sleep(1)

        #  send reply back to client
        response = b"World"
        print("Send response to client: %s" % response)
        server.send(response)