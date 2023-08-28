import socket


class Client:
    def __init__(self, host: str = None, port: int = None):
        # o achando feio isso aqui mas é para um bem maior (1)
        if host and port is not None:
            self.__host: str = host
            self.__port: int = port
            self.__socket: socket = socket.socket()
            self.__socket.connect((self.__host, self.__port))



    def get_socket(self) -> socket:
        return self.__socket

    def set_host(self, host: str) -> None:
        self.__host = host

    def get_host(self) -> str:
        return self.__host

    def set_port(self, port: int) -> None:
        self.__port = port

    def get_port(self) -> int:
        return self.__port

    def connect(self, host: str, port: int) -> None:
        self.__socket.connect((host, port))

    def close(self) -> None:
        self.__socket.close()

    def __str__(self) -> str:
        return f"Client(host={self.__host}, port={self.__port})"
