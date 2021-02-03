from Graph import Graph
from Dijkstra import dijkstra
from Visual import plot_number, plot_path, sub_plot_path, show
import sys

g = Graph()

class Request:

    def __init__(self, time: float, source_id: int, destination_id: int, path_pair=[], path_pair_times=[], status= False):
        self.start_time = time
        self._time = time
        self.source = g.get_vertex(source_id)
        self.destination = g.get_vertex(destination_id)
        self._path_pair = path_pair
        self._path_pair_times = path_pair_times
        self.status = status

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if self._time < value:
            self._time = value

    @property
    def path_pair(self):
        return self._path_pair

    @path_pair.setter
    def path_pair(self, value):
        self._path_pair = value

    @property
    def path_pair_times(self):
        return self._path_pair_times

    @path_pair_times.setter
    def path_pair_times(self, value):
        self._path_pair_times = value

    def __lt__(self, obj):
        return self.time < obj.time

    def __int__(self):
        return int(self.time) + self.source.id + self.destination.id

    def __repr__(self):
        return f'({self.time}, {self.source}, {self.destination}, {self.status})'
        

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
    request = Request(*req)
    requests.append(request)

plot_number(len(requests))

vertex_list = []

for request in requests:

    i = 0
    while i < len(vertex_list):
        if vertex_list[i][1] <= request.time:
            g.decrease_edge_traffic(*vertex_list[i][0])
            del vertex_list[i]
            i -= 1
        i += 1
    
    if request.source:
        start = request.source
        destination = request.destination
        start.time = request.time
        dijkstra(g, start, destination)
        path = g.get_path(start, destination)
        print(f'Request Path for Request at time ({request.time}):', path)
        path_pair = list(zip(path[:-1], path[1:]))
        request.path_pair = path_pair
        request.path_pair_times = g.calculate_time_list(path_pair)
        for v1, v2 in path_pair:
            g.increase_edge_traffic(v1, v2)
        sub_plot_path(g, path_pair, request)
        # plot_path(g, path_pair, request)
        vertex_list.extend(list(zip(request.path_pair, request.path_pair_times)))

        g.reset_dist_nodes()

show()