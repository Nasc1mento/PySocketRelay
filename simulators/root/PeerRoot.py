import sys
from models.Client import Client
from models.Server import Server
from models.Peer import Peer
sys.path.append('../../models/')

server: Server = Server('0.0.0.0', 8072)
client: Client = Client('0.0.0.0', 8098)
peer: Peer = Peer(server, client)

while True:
    msg: str = input('message: ')
    peer.get_client().get_socket().send(msg.encode())












