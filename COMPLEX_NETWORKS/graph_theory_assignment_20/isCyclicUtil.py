#whether the grap is cyclic or acyclic
def is_cyclic_util(graph, node, passed, rec_stack):
    passed[node] = True
    rec_stack[node] = True

    for i in graph[node]:
        if not passed[i]:
            if is_cyclic_util(graph, i, passed, rec_stack):
                return True
        elif rec_stack[i]:
            return True

    rec_stack[node] = False
    return False