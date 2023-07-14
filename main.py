from data_structures.Graph import Graph

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 2)
# graph.add_edge(1, 3)
graph.add_edge(1, 4)

for edge in graph.get_edges():
    print("Source:", edge.get_source().get_key())
    print("Destination:", edge.get_destination().get_key())
    print()
