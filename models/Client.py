import socket


class Client:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket()
        self.__socket.connect((self.__host, self.__port))

    def get_socket(self):
        return self.__socket


