from collections import defaultdict
import sys

class Graph:

    class Node:

        def __init__(self, id, lat, long, dist=sys.maxsize, prev=None):
            self.id = id
            self.lat = lat
            self.long = long
            self._dist = dist
            self._prev = prev

        @property
        def dist(self):
            return self._dist

        @property
        def prev(self):
            return self._prev

        @dist.setter
        def dist(self, value):
            self._dist = value

        @prev.setter
        def prev(self, value):
            self._prev = value

        def __lt__(self, obj):
            return self.dist < obj.dist

        def __int__(self):
            return self.id

        def __repr__(self):
                return '(' + str(self.id) + ', ' + str(self.dist) + ', ' + str(self.prev) + ')'

    def __init__(self, nodes= list()):
        self.nodes = nodes
        self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex_id, vertex_lat, vertex_long):
        self.nodes.append(self.Node(vertex_id, vertex_lat, vertex_long))

    def add_edge(self, v1, v2, weight: int):
        self.adjacency_list[v1.id].append((v2, weight))
        self.adjacency_list[v2.id].append((v1, weight))

    def get_vertex_neighbors(self, vertex):
        if vertex in self.nodes:
            return self.adjacency_list[vertex.id]