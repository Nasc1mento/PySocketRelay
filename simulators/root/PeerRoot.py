import socket
import threading
import time
from models.Server import Server
from models.Peer import Peer

server: Server = Server('0.0.0.0', 8074)
peer: Peer = Peer(server)


def send(sock_peer: socket, address: tuple):
    print(f'connected to {address}')
    while True:
        try:
            msg: str = f'ola do root {address}'
            sock_peer.send(msg.encode())
            time.sleep(5)
        except (ConnectionResetError, socket.error):
            print(f'pipe broken with {address}')
            break
    sock_peer.close()


while True:
    [sock, addr] = peer.get_server().get_socket().accept()
    threading.Thread(target=send, args=(sock, addr,)).start()
