import os
import collections
import copy
import uniqueOutputDir
import generatingGraphs
import isCyclic
import saveGeneratedGraphs
import saveAnalyzedResult
import saveMetrics

def generate_graph_and_analysis(graph_order, graph_density):
    for i in range(16):
        output_dir = uniqueOutputDir.unique_output_directory()
        graph = generatingGraphs.generating_random_graphs(graph_order, graph_density)
        num_nodes = len(graph)
        edges = sum(len(adj_list) for adj_list in graph.values())
        node_degrees = [len(adj_list) for adj_list in graph.values()]

        avg_degree = sum(node_degrees) / num_nodes

        sorted_degrees = sorted(enumerate(node_degrees), key=lambda x: x[1])

        top_5_highest_degrees = sorted_degrees[-5:]
        top_5_lowest_degrees = sorted_degrees[:5]

        selected_nodes = [node for node, _ in top_5_highest_degrees + top_5_lowest_degrees]
        in_degrees = [len([n for n, adj_list in graph.items() if node in adj_list]) for node in selected_nodes]
        out_degrees = [len(graph[node]) for node in selected_nodes]

        # Here, we'll use a 10 bits bins where the bins are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        degree_bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        degree_counts = collections.Counter(node_degrees)
        in_degree_counts = collections.Counter(in_degrees)
        out_degree_counts = collections.Counter(out_degrees)

        # Checking if the graph is cyclic
        cyclic = isCyclic.is_cyclic(graph)
        if cyclic:
            graph_is = "The graph is cyclic."
        else:
            graph_is = "The graph is acyclic."


        sum_of_in_degrees = sum(in_degrees)
        sum_of_out_degrees = sum(out_degrees)

        #analysis_results
        analysis_results = {
            'size': (num_nodes, edges),
            'average_degree': avg_degree,
            'top_5_highest_degrees': [item[1] for item in top_5_highest_degrees],
            'top_5_lowest_degrees': [item[1] for item in top_5_lowest_degrees],
            'in_degrees': in_degrees,
            'out_degrees': out_degrees, 
            'degree_counts': dict(degree_counts),
            'in_degree_counts': dict(in_degree_counts),
            'out_degree_counts': dict(out_degree_counts),
            'graph_is' : graph_is,
            'sum_of_in_degrees': sum_of_in_degrees,
            'sum_of_out_degrees': sum_of_out_degrees,
    
        }


        graph_output_file = os.path.join(output_dir, f"graph_{i}.txt")
        saveGeneratedGraphs.save_generated_graphs_as_file(graph, graph_output_file)

        analysis_output_file = os.path.join(output_dir, f"analysis_{i}.txt")
        saveAnalyzedResult.save_analyzed_results_as_file(analysis_results, graph_output_file)

        summary_metrics = copy.deepcopy(analysis_results)

        for key, values in summary_metrics.items():
            if isinstance(values, (list, tuple)):
                # Handle lists separately
                average = sum(values) / len(values)
                standard_deviation = (sum((x - average) ** 2 for x in values) / len(values)) ** 0.5
                summary_metrics[key] = {
                    'average': average,
                    'std_deviation': standard_deviation
                }

        # Summary metrics to a text file
        metrics_file = os.path.join(output_dir, "summary_metrics.txt")
        saveMetrics.save_metrics_as_file(summary_metrics, metrics_file)