import ast
import socket
import threading

from models.Client import Client
from models.Peer import Peer
from models.Server import Server
from models.Tracker import Tracker

tracker: Tracker = Tracker(Tracker.get_local_ip(), 8666)


def add(sock_peer: socket, address: tuple):
    print(f'add peer: {address}')
    try:
        msg: tuple = ast.literal_eval(sock_peer.recv(1024).decode())

        peer: Peer = Peer()

        server_peer: Server = Server()
        server_peer.set_host(msg[0][0])
        server_peer.set_port(msg[0][1])

        client: Client = Client()
        client.set_host(msg[1][0])
        client.set_port(msg[1][1])

        peer.set_server(server_peer)
        peer.set_client(client)

        tracker.add(peer)
        peers = tracker.get_list()

        print(tracker.get_list())

    except (ConnectionResetError, socket.error):
        print(f'err')

    sock_peer.close()


while True:
    [sock, addr] = tracker.get_server().accept()
    threading.Thread(target=add, args=(sock, addr,)).start()