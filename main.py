from models.Peer import Peer
from models.Server import Server
from models.Client import Client

server1 = Server('localhost', 8071)
server2 = Server('localhost', 8070)
client1 = Client('localhost', 8070)
client2 = Client('localhost', 8071)

peer1 = Peer(server1, client1)
peer2 = Peer(server2, client2)

peer1.send('Hello, world!')
print(peer2.receive())






