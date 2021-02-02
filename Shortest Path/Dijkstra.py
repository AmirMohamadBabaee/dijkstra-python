from Graph import Graph
from MinHeap import MinHeap

def dijkstra(graph: Graph, source: Graph.Node, destination: Graph.Node):
    source.dist = 0
    unexplored = MinHeap(array=graph.nodes)
    explored = set()
    while destination not in explored:
        v = unexplored.get_minimum()
        unexplored.delete_min()
        explored.add(v)
        neighbors = graph.get_vertex_neighbors(v)
        if neighbors:
            for neighbor in neighbors:
                w, weight, _ = neighbor
                if v.dist + weight < w.dist:
                    w.dist = v.dist + weight
                    w.prev = v
                    unexplored.modify(w, w)
