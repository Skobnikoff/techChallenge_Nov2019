import time
import zmq


def partition_work(matrix_1, matrix_2):
    tasks = {}
    matrix_2_transposed = list(map(list, zip(*matrix_2)))
    for row_index, row_matrix_1 in enumerate(matrix_1):
        for col_index, col_matrix_2 in enumerate(matrix_2_transposed):
            task = {"data": (row_matrix_1, col_matrix_2),
                    "indexes": (row_index, col_index),
                    "status": "todo",
                    "task_id": '{}_{}'.format(row_index, col_index)
                    }
            tasks[task["task_id"]] = task
    return tasks


if __name__ == '__main__':

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

    while True:
        #  wait for client request
        print("Waiting for a request from client...")

        client_input_data = server.recv_json()
        print("Received request: {}".format(client_input_data))

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
            task_id = slave_response["task_id"]
            print("Got results for the task #{}".format(task_id))
            tasks[task_id]["result"] = slave_response["result"]

        # assemble results
        result_matrix = []
        matrix_shape = len(client_input_data["matrix_1"])
        for row_index in range(matrix_shape):
            result_matrix.append([0]*matrix_shape)

        for task in tasks.values():
            row_index, col_index = task["indexes"]
            result_matrix[row_index][col_index] = task["result"]

        time.sleep(1)

        #  send reply back to client
        print("Send response to client: {}".format(result_matrix))
        server.send_json(result_matrix)