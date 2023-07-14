from data_structures.Node import Node


class Edge:

    def __init__(self, source, destination):
        self.__source: Node = source
        self.__destination: Node = destination

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def __eq__(self, other):
        return self.__source == other.__source and self.__destination == other.__destination

    def __hash__(self):
        return hash((self.__source, self.__destination))

