import pickle
import socket
import threading
import time

from models.Client import Client
from models.Server import Server
from models.Peer import Peer
from models.Tracker import Tracker


server: Server = Server(Tracker.get_local_ip(), 8074)
client: Client = Client(Tracker.get_local_ip(), 8666)
peer: Peer = Peer(server)

identifier_server = server.get_socket().getsockname()
identifier_client = client.get_socket().getsockname()
client.get_socket().send(str([identifier_server, identifier_client]).encode())
client.get_socket().close()


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
