class Node:

    def __init__(self, key, neighbor1, neighbor2):
        self.__key = key
        self.__neighbor1: Node = neighbor1
        self.__neighbor2: Node = neighbor2

    def get_key(self):
        return self.__key

    def get_neighbors(self):
        return [self.__neighbor1, self.__neighbor2]

    def add_neighbor(self, node):
        if self.__neighbor1 is None:
            self.__neighbor1 = node
        elif self.__neighbor2 is None:
            self.__neighbor2 = node

    def not_usable(self):
        return self.__neighbor1 is not None and self.__neighbor2 is not None

    def __eq__(self, other):
        return self.__key == other.__key

    def __hash__(self):
        return hash(self.__key)

