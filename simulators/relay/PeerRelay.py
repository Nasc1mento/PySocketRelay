import sys
import threading
import socket
from models.Client import Client
from models.Server import Server
from models.Peer import Peer
sys.path.append('../../models/')

server: Server = Server('0.0.0.0', 8098)
client: Client = Client('0.0.0.0', 8074)
peer: Peer = Peer(None, client, False)


def relay():
    while True:
        msg: str = peer.get_client().get_socket().recv(1024).decode()
        if not msg:
            break
        print(f'msg: {msg})')
        if peer.is_relay():
            [sock, addr] = server.get_socket().accept()
            threading.Thread(target=send, args=(sock, addr, msg,)).start()


def send(sock_peer: socket, address: tuple, msg: str):
    print(f'connected to {address}')
    sock_peer.send(msg.encode())


while True:
    relay()













