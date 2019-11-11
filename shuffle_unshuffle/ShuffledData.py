import csv
import random
import sys

class ShuffledData:

    def __read_csv(self, file_path):
        table = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                table.append(line)
        return table

    def __init__(self, file_path):
        self.table = self.__read_csv(file_path)
        self.__horizon_shuffle_lst = []
        self.__vertical_shuffle_lst = []

    def __transpose(self, lst):
        return list(map(list, zip(*lst)))

    # shuffle
    def __rotate(self, lst, n):
        if n > 0:
            n = n % len(lst)
        else:
            n = -(-n % len(lst))
        return lst[n:] + lst[:n]

    def __shuffle_1d(self, table):
        width = len(table[0])
        shuffle_lst = []
        for i, line in enumerate(table):
            rand_move = random.randint(-width * 10, width * 10)
            shuffle_lst.append(rand_move)
            table[i] = self.__rotate(line, rand_move)

        return shuffle_lst, table

    def shuffle(self):
        self.__horizon_shuffle_lst, self.table = self.__shuffle_1d(self.table)
        self.table = self.__transpose(self.table)
        self.__vertical_shuffle_lst, self.table = self.__shuffle_1d(self.table)
        self.table = self.__transpose(self.table)

    # unshuffle
    def __rotate_back(self, lst, n):
        if n > 0:
            n = -(n % len(lst))
        else:
            n = -n % len(lst)
        return lst[n:] + lst[:n]

    def __unshuffle_1d(self, shuffle_lst, table):
        for i, rand_move in enumerate(shuffle_lst):
            table[i] = self.__rotate_back(table[i], rand_move)
        return table

    def unshuffle(self):
        self.table = self.__transpose(self.table)
        self.table = self.__unshuffle_1d(self.__vertical_shuffle_lst, self.table)
        self.table = self.__transpose(self.table)
        self.table = self.__unshuffle_1d(self.__horizon_shuffle_lst, self.table)


def write_csv(data, file_path):
    with open(file_path, 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in data:
            writer.writerow(line)


if __name__ == '__main__':

    file_path = sys.argv[1]

    file = ShuffledData(file_path)

    file.shuffle()
    out_file_path = file_path.split('.csv')[0] + "_shuffled.csv"
    write_csv(data=file.table, file_path=out_file_path)
    print("Shuffled file: {}".format(out_file_path))

    file.unshuffle()
    out_file_path = file_path.split('.csv')[0] + "_unshuffled.csv"
    write_csv(data=file.table, file_path=out_file_path)
    print("Unshuffled file: {}".format(out_file_path))