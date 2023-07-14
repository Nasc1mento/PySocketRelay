from data_structures.Edge import Edge
from data_structures.Node import Node
# TODO: Cycle detection, remove edges, shortest path, etc.


class Graph:

    def __init__(self):
        self.__nodes: dict[Node, Node] = {}
        self.__edges: dict[Edge, Edge] = {}

    def get_nodes(self) -> list[Node]:
        return list(self.__nodes.values())

    def get_node(self, key) -> Node | None:
        return self.__nodes.get(key)

    def add_node(self, key) -> Node:
        node: Node = Node(key)
        self.__nodes[key] = node
        return node

    def remove_node(self, key) -> Node | None:
        pass

    def add_edge(self, source, destination) -> Edge | None:
        if source not in self.__nodes:
            self.add_node(source)
        if destination not in self.__nodes:
            self.add_node(destination)

        edge: Edge = Edge(self.__nodes[source], self.__nodes[destination])

        if edge in self.__edges:
            return

        if self.__nodes[source].full():
            return

        self.__edges[edge] = edge
        self.__nodes[source].add_neighbor(self.__nodes[destination])
        return edge

    def remove_edge(self, source, destination) -> Edge | None:
        if source not in self.__nodes:
            return
        if destination not in self.__nodes:
            return

        edge: Edge = Edge(self.__nodes[source], self.__nodes[destination])

        if edge not in self.__edges:
            return

        self.__edges.pop(edge)
        self.__nodes[source].remove_neighbor(self.__nodes[destination])
        return edge

    def get_edges(self) -> list[Edge]:
        return list(self.__edges.keys())

    def __iter__(self):
        return iter(self.__nodes.values())
