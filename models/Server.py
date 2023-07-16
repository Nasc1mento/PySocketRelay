import socket


class Server:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen(100)

    def get_socket(self):
        return self.__socket

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def __str__(self):
        return f"Server(host={self.__host}, port={self.__port})"