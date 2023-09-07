# To save the graph as text file
def save_generated_graphs_as_file(graph, output_file):
    with open(output_file, 'w') as f:
        f.write("Random Generated Graph :\n")
        for node, adj_nodes in graph.items():
            line = f"{node}: {', '.join(map(str, adj_nodes))}\n"
            f.write(line)