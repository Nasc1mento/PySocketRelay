import socket


class Server:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen(100)

    @staticmethod
    def receive(sock: socket) -> str:
        return sock.recv(1024).decode()

    def accept(self) -> socket:
        return self.__socket.accept()

    def close(self) -> None:
        self.__socket.close()


