import socket


class Server:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__sock: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind((self.__host, self.__port))
        self.__sock.listen()

    def accept(self) -> socket:
        return self.__sock.accept()

    def receive(self, sock: socket) -> str:
        return sock.recv(1024).decode()

    def close(self) -> None:
        self.__sock.close()


