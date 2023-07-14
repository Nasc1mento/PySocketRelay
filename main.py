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


def test_server() -> None:
    server: Server = Server('localhost', 8080)
    client1: Client = Client('localhost', 8080)

    [client, address] = server.accept()
    print("Client connected:", address)

    client1.send("Hello, world!")

    print(server.receive(client))


test_server()
