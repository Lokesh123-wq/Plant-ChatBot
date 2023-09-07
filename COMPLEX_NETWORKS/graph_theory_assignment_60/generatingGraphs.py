import random

def generating_random_graphs(graph_order, graph_density):
    graph = {node: [] for node in range(graph_order)}
    edges = int(graph_density * graph_order * (graph_order - 1))

    edge_count = 0
    while edge_count < edges:
        source = random.randint(0, graph_order - 1)
        destination = random.randint(0, graph_order - 1)

        if source != destination and destination not in graph[source]:
            graph[source].append(destination)
            edge_count += 1

    return graph