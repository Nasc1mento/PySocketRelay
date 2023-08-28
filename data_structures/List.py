from models.Peer import Peer
from data_structures.Node import Node


class List:

    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None

    def add(self, peer:Peer):
        # new_node = Node()
        # new_node.set_peer(peer)
        #
        # if self.__head is None:
        #     self.__head = new_node
        #     self.__tail = new_node
        # else:
        #     new_node_srv_port: int = self.__head.get_peer().get_server().get_port()
        #     new_node_srv_host: str = self.__head.get_peer().get_server().get_host()
        #
        #     self.__tail.set_next(new_node)
        #     new_node.set_prev(self.__tail)
        #     self.__tail = new_node
        #
        #     self.__tail.get_peer().get_client().connect(new_node_srv_host, new_node_srv_port)
        print("hello")
    def __str__(self) -> str:
        return f"List(head={self.__head}, tail={self.__tail})"
