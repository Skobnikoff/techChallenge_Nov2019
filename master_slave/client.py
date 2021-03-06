import zmq
import time


if __name__ == '__main__':

    # input
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

    # init 0MQ context and define sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #  send request to master
    socket.send_json(input_data)
    print("CLIENT: Sent request to Master: {}".format(input_data))

    time.sleep(1)

    #  wait for response from master
    response = socket.recv_json()
    print("CLIENT: Received response from Master: {}".format(response))