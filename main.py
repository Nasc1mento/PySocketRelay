import threading

from communication.Client import Client
from communication.Server import Server
from data_structures.Graph import Graph


#
# graph: Graph = Graph()
# graph.add_edge(1, 2)
# graph.add_edge(1, 2)
# graph.add_edge(1, 4)
# graph.remove_edge(1, 4)
# graph.remove_edge(1, 2)
# graph.add_edge(1, 2)
#
# for node in graph:
#     print("Node:", node.get_key())
#     print("Neighbors:", [neighbor for neighbor in node.get_neighbors()])
#     print()
#
# for edge in graph.get_edges():
#     print("Source:", edge.get_source().get_key())
#     print("Destination:", edge.get_destination().get_key())
#     print()

# TODO: Testar comunicação com o servidor e clientes

[host, port] = ['localhost', 8090]

server: Server = Server(host, port)
client1: Client = Client(host, port)
client2: Client = Client(host, port)
client1.send('Hello from client 1')
client2.send('Hello from client 2')


def test_server() -> None:

    while True:
        [client, addr] = server.accept()
        print(f'client connected {addr}\n')

        threading.Thread(target=loop_client_receive, args=(client, addr)).start()


def loop_client_receive(client: Client, addr: tuple[str, int]) -> None:
    while True:
        print(f'client {addr} sent: {server.receive(client)}')


test_server()
