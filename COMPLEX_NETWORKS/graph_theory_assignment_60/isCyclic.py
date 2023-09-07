import isCyclicUtil

def is_cyclic(graph):
    num_nodes = len(graph)
    passed = [False] * num_nodes
    rec_stack = [False] * num_nodes

    for node in range(num_nodes):
        if not passed[node]:
            if isCyclicUtil.is_cyclic_util(graph, node, passed, rec_stack):
                return True

    return False