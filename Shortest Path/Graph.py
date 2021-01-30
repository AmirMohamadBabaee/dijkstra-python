from collections import defaultdict
import sys

class Graph:

    class Node:

        def __init__(self, id, lat, long, dist=sys.maxsize, prev=None):
            self.id = id
            self.lat = lat
            self.long = long
            self.dist = dist
            self.prev = prev

        @dist.setter
        def dist(self, value):
            self.dist = value

        @prev.setter
        def prev(self, value):
            self.prev = value

        def __lt__(self, obj: self.__class__):
            return self.dist < obj.dist

        def __repr__(self):
                return '(' + str(self.name) + ', ' + str(self.dist) + ', ' + str(self.prev) + ')'

    def __init__(self, nodes: set):
        self.nodes = nodes
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex: self.Node):
        self.nodes.add(vertex)

    def add_edge(self, v1: self.Node, v2: self.Node, weight: int):
        self.adjacency_list[v1.id].append((v2, weight))
        self.adjacency_list[v2.id].append((v1, weight))

    def get_vertex_neighbors(self, vertex: self.Node):
        if vertex in self.nodes:
            return self.adjacency_list[vertex.id]