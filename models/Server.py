import socket


class Server:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen()

    def get_socket(self):
        return self.__socket
