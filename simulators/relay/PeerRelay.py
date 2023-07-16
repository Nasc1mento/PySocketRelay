import sys
import threading
import socket
from models.Client import Client
from models.Server import Server
from models.Peer import Peer
sys.path.append('../../models/')

server = Server('0.0.0.0', 8098)
client = Client('0.0.0.0', 8099)
peer = Peer(server, client)


def relay(sock_peer: socket, address: tuple):
    while True:
        msg: str = sock_peer.recv(1024).decode()
        if not msg:
            break
        print(f'msg: {msg} addr: {address}')
        if peer.is_relay():
            peer.get_client().send(msg.encode())


while True:
    [sock, addr] = peer.get_server().accept()
    threading.Thread(target=relay, args=(sock, addr,)).start()













