import threading
import socket
from models.Client import Client
from models.Server import Server
from models.Peer import Peer
from models.Tracker import Tracker

server: Server = Server('0.0.0.0', Tracker.get_random_port())
client: Client = Client('0.0.0.0', 8074)
peer: Peer = Peer(None, client, True)


def relay():
    while True:
        msg: str = peer.get_client().get_socket().recv(1024).decode()
        if not msg:
            break
        print(f'msg: {msg})')
        if peer.is_relay():
            [sock, addr] = server.get_socket().accept()
            #threading?
            send(sock, addr, msg,)


def send(sock_peer: socket, address: tuple, msg: str):
    print(f'connected to {address}')
    sock_peer.send(msg.encode())


while True:
    threading.Thread(target=relay).start()
