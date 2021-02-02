from Graph import Graph
from Dijkstra import dijkstra
from Visual import plot_number, plot_path, sub_plot_path, show
import sys

g = Graph()
n, m = list(map(int, input().split()))

for _ in range(n):
    id, lat, long = list(map(float, input().split()))
    id = int(id)
    g.add_vertex(id, lat, long)

for _ in range(m):
    v1_id, v2_id = list(map(int, input().split()))
    g.add_edge_by_id(v1_id, v2_id)

requests = []

# Request 
while True:
    req = list(map(float, input().split()))
    if req == []:
        break
    req = [req[0], int(req[1]), int(req[2])]
    req.extend([None, sys.maxsize])
    requests.append(req)

plot_number(len(requests))
requests.append((sys.maxsize, None, None, None, sys.maxsize))


for request in requests:

    for req in requests:
        if req[4] < request[0]:
            for v1, v2 in req[3]:
                g.decrease_edge_traffic(v1, v2)
        elif req[4] == sys.maxsize:
            break
    
    if request[1]:
        start = g.get_vertex(request[1])
        destination = g.get_vertex(request[2])
        dijkstra(g, start, destination)
        path = g.get_path(start, destination)
        path_pair = list(zip(path[:-1], path[1:]))
        request[3] = path_pair
        request[4] = request[0] + g.calculate_time(path_pair)
        for v1, v2 in path_pair:
            g.increase_edge_traffic(v1, v2)
        sub_plot_path(g, path_pair, request)
        # plot_path(g, path_pair, request)

        g.reset_dist_nodes()

show()