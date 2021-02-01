from collections import defaultdict
import sys
import math
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

    def add_edge_by_node(self, v1, v2, weight: int):
        traffic = 0
        self.adjacency_list[v1.id].append([v2, weight, traffic])
        self.adjacency_list[v2.id].append([v1, weight, traffic])

    def add_edge_by_id(self, v1_id, v2_id, weight=None):
        v1 = self.get_vertex(v1_id)
        v2 = self.get_vertex(v2_id)

        if v1 and v2:
            if not weight:
                weight = self.get_Euclidean_distance(v1, v2)
            self.add_edge_by_node(v1, v2, weight)

    def get_vertex(self, id):
        for node in self.nodes:
            if node.id == id:
                return node

    def get_vertex_neighbors(self, vertex):
        if vertex in self.nodes:
            return self.adjacency_list[vertex.id]

    def get_edge(self, v1, v2):
        v1_neighbors = self.get_vertex_neighbors(v1)
        if v1_neighbors:
            for neighbor in v1_neighbors:
                if neighbor[0] == v2:
                    return neighbor
    
    def calculate_edge_weight(self, edge, distance, traffic_factor=0.3):
        if edge:
            traffic = edge[2]
            weight = distance + (1 + traffic_factor * traffic)
            edge[1] = weight

    def increase_edge_traffic(self, v1, v2):
        edge1 = edge = self.get_edge(v1, v2)
        edge2 = edge = self.get_edge(v2, v1)
        if edge1 and edge2:
            edge1[2] += 1
            edge2[2] += 1
            distance = self.get_Euclidean_distance(v1, v2)
            self.calculate_edge_weight(edge1, distance)
            self.calculate_edge_weight(edge2, distance)

    def decrease_edge_traffic(self, v1, v2):
        edge1 = edge = self.get_edge(v1, v2)
        edge2 = edge = self.get_edge(v2, v1)
        if edge1 and edge2 and edge1[2] + edge2[2] >= 2:
            edge1[2] -= 1
            edge2[2] -= 1
            distance = self.get_Euclidean_distance(v1, v2)
            self.calculate_edge_weight(edge1, distance)
            self.calculate_edge_weight(edge2, distance)

    def get_Euclidean_distance(self, v1, v2):
        return math.sqrt((v1.lat - v2.lat) ** 2 + (v1.long - v2.long) ** 2)