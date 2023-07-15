from models.Client import Client


class Node:

    def __init__(self, key: Client, neighbor1=None, neighbor2=None):
        self.__key: Client = key
        self.__neighbor1: Node = neighbor1
        self.__neighbor2: Node = neighbor2

    def get_key(self):
        return self.__key

    def get_neighbors(self) -> list['Node']:
        return [self.__neighbor1, self.__neighbor2]

    def add_neighbor(self, node) -> None:
        if self.__neighbor1 is None:
            self.__neighbor1 = node
        elif self.__neighbor2 is None:
            self.__neighbor2 = node

    def remove_neighbor(self, node) -> None:
        if self.__neighbor1 == node:
            self.__neighbor1 = None
        elif self.__neighbor2 == node:
            self.__neighbor2 = None

    def full(self) -> bool:
        return self.__neighbor1 is not None and self.__neighbor2 is not None

    def __eq__(self, other: 'Node') -> bool:
        return self.__key == other.__key

    def __hash__(self) -> int:
        return hash(self.__key)
