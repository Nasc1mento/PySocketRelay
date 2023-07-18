import socket


class Server:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen(100)

    def get_socket(self) -> socket:
        return self.__socket

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port

    def close(self) -> None:
        self.__socket.close()

    def __str__(self) -> str:
        return f"Server(host={self.__host}, port={self.__port})"