from data_structures.Edge import Edge
from data_structures.Node import Node
# TODO: Verify cycle detection, remove edges, shortest path, etc.


class Graph:

    def __init__(self):
        self.__nodes: dict[Node, Node] = {}
        self.__edges: dict[Edge, Edge] = {}

    def get_nodes(self):
        return self.__nodes.values()

    def get_node(self, key):
        return self.__nodes.get(key)

    def add_node(self, key):
        node = Node(key, None, None)
        self.__nodes[key] = node
        return node

    def add_edge(self, source, destination):
        if source not in self.__nodes:
            self.add_node(source)
        if destination not in self.__nodes:
            self.add_node(destination)

        edge: Edge = Edge(self.__nodes[source], self.__nodes[destination])

        if edge in self.__edges:
            return

        if self.__nodes[source].not_usable():
            return

        self.__edges[edge] = edge
        self.__nodes[source].add_neighbor(self.__nodes[destination])

    def get_edges(self):
        return self.__edges.keys()

    def __iter__(self):
        return iter(self.__nodes.values())
