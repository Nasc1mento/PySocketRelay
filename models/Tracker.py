import socket
import random
from typing import Type

from data_structures.List import List
from models.Peer import Peer


class Tracker:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen()
        self.__list = List

    def add(self, peer: Peer):
        self.__list.add(peer)

    def get_list(self) -> Type[List]:
        return self.__list

    def get_server(self) -> socket:
        return self.__socket

    def close(self) -> None:
        self.__socket.close()

    @classmethod
    def get_random_port(cls) -> int:
        return random.randint(1024, 65535)

    @classmethod
    def get_local_ip(cls):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
        except:
            local_ip = 'N/A'
        finally:
            s.close()
        return local_ip


