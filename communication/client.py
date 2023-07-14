from socket import socket


class Client:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket()
        self.__socket.connect((self.__host, self.__port))

    def send(self, data: str) -> None:
        self.__socket.send(data.encode())

    def receive(self) -> str:
        return self.__socket.recv(1024).decode()

    def close(self) -> None:
        self.__socket.close()

