import sys
from models.Client import Client
from models.Server import Server
from models.Peer import Peer
sys.path.append('../../models/')

server = Server('0.0.0.0', 8098)
client = Client('0.0.0.0', 8099)
peer = Peer(server, client)

while True:
    msg = input('message: ')
    peer.get_client().send(msg.encode())












