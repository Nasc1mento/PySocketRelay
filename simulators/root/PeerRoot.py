import socket
import threading
import time
from models.Server import Server
from models.Peer import Peer

server: Server = Server('0.0.0.0', 8074)
peer: Peer = Peer(server)


def send(sock_peer: socket, address: tuple):
    print(f'connected to {address}')
    threading.Thread(target=send_aux, args=(sock_peer, address,)).start()


def send_aux(sock_peer: socket, address: tuple):
    while True:
        msg: str = f'ola do root{address}'
        sock_peer.send(msg.encode())
        time.sleep(5)


while True:
    [sock, addr] = peer.get_server().get_socket().accept()
    threading.Thread(target=send, args=(sock, addr,)).start()
