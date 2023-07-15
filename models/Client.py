import socket


class Client:
    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen()

    def connect(self, host: str, port: int) -> None:
        self.__socket.connect((host, port))

    def send(self, message: str) -> None:
        self.__socket.send(message.encode())

    def receive(self) -> str:
        return self.__socket.recv(1024).decode()

    def __str__(self):
        return f'{self.__host}:{self.__port}'