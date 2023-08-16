from models.Peer import Peer


class Node:

    def __init__(self):
        self.__next:Node = None
        self.__prev:Node= None
        self._peer:Node = None


    def set_next(self, next:'Node') -> None:
        self.__next = next

    def get_next(self) -> 'Node':
        return self.__next
    
    def set_prev(self, prev:'Node') -> None:
        self.__prev = prev

    def get_prev(self) -> 'Node':
        return self.__prev
    

    def set_peer(self, peer:Peer) -> Peer:
        self.__peer = peer

    def get_peer(self) -> None:
        return self.__peer
        

    def __str__(self) -> str:
        return f"Node(key={self.__peer}"

    def __eq__(self, other: 'Node') -> bool:
        return self.__peer == other.__peer

    def __hash__(self) -> int:
        return hash(self.__peer)
