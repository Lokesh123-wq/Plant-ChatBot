# Function to save the graph 
def save_generated_graphs_as_file(graph, output_file):
    with open(output_file, 'w') as f:
        f.write("Random Generated Graphs :\n")
        for node, adj_nodes in graph.items():
            line = f"{node}: {', '.join(map(str, adj_nodes))}\n"
            f.write(line)