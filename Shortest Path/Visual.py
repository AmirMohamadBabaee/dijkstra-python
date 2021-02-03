import matplotlib.pyplot as plt
import math

fig = None
ax = None
counter = 0

def plot_number(req_num):
    global fig, ax
    fig, ax = plt.subplots(math.ceil(req_num/2), 2, figsize=(25,20), squeeze=False)

def plot_map(graph):
    edges = graph.adjacency_list
    for id, neighbor in edges.items():
        if neighbor:
            node = graph.get_vertex(id)
            for neighbor_node in neighbor:
                next_node = neighbor_node[0]
                x = (node.long, next_node.long)
                y = (node.lat, next_node.lat)
                if fig:
                    ax[counter//2][counter%2].plot(x, y, label='2', color='blue', marker='.')
                else:
                    plt.plot(x, y, color='blue', marker='.', linewidth=0.5, markersize=3)
                # ax[counter//2][counter%2].annotate(f'{node.id}', (x[0], y[0]))
                # ax[counter//2][counter%2].annotate(f'{next_node.id}', (x[1], y[1]))

def plot_path(graph, path_pair, request):
    X = []
    Y = []
    global counter
    for v1, v2 in path_pair:
        X.append([v1.long, v2.long])
        Y.append([v1.lat, v2.lat])

    plot_map(graph)
    plt.title(f'Request ({counter + 1})')
    l = None
    for i in range(len(X)):
        l, = plt.plot(X[i], Y[i], label=f'req time: {request.start_time}\nend time: {round(request.path_pair_times[-1], 2)}' if i == 0 else str(), linewidth=6, alpha=0.7, color='green', marker='^', markeredgecolor='black')
    
    plt.legend(loc='upper right')
    counter += 1
    show()

def sub_plot_path(graph, path_pair, request):
    X = []
    Y = []
    global counter
    for v1, v2 in path_pair:
        X.append([v1.long, v2.long])
        Y.append([v1.lat, v2.lat])

    plot_map(graph)
    ax[counter//2][counter%2].set_title(f'Request ({counter + 1})')
    l = None
    for i in range(len(X)):
        l, = ax[counter//2][counter%2].plot(X[i], Y[i], label=f'request {counter + 1}', linewidth=6, alpha=0.7, color='green', marker='^', markeredgecolor='black')
    
    ax[counter//2][counter%2].legend(handles=[l] ,labels=[f'req time: {request.start_time}\nend time: {round(request.path_pair_times[-1], 2)}'], loc='upper right')
    counter += 1

def show():
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()