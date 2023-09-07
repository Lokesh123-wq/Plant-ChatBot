import os
import random
import time
import graphGenAndAnalyze

# Function for input
def main():
    graph_order = int(input("Enter the order of the graph : "))
    graph_density = float(input("Enther the graph density : "))
    graphGenAndAnalyze.generate_graph_and_analysis(graph_order, graph_density)

if __name__ == "__main__":
    main()