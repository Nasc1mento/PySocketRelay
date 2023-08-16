from models.Peer import Peer
from data_structures.Node import Node
class CircularList:

    def __init__(self) -> None:
        self.__first:Node = None



    def add(self, peer:Peer):
        new_node = Node()
        new_node.set_peer(peer)

        if self.__first is None:
            self.__first = new_node
        else:
            self.__first.set_prev(new_node)
            new_node.set_next(self.__first)

