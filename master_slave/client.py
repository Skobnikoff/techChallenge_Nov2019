import zmq
import time


if __name__ == '__main__':

    # get input
    # TODO

    # init 0MQ context and define sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  send request to master
    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_2 = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    input_data = {'matrix_1': matrix_1, 'matrix_2': matrix_2}

    print("Send request: %s" % input_data)
    socket.send_json(input_data)

    time.sleep(1)

    #  wait for response from master
    response = socket.recv()
    print("Received response: %s" % response)