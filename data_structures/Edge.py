from data_structures.Node import Node


class Edge:

    def __init__(self, source: Node, destination: Node):
        self.__source: Node = source
        self.__destination: Node = destination

    def get_source(self) -> Node:
        return self.__source

    def get_destination(self) -> Node:
        return self.__destination

    def __eq__(self, other: 'Edge') -> bool:
        return self.__source == other.__source and self.__destination == other.__destination

    def __hash__(self) -> int:
        return hash((self.__source, self.__destination))

