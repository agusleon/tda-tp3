from digraph import Digraph

#Edmonds-Karp Algorithm
def max_flow(graph, residual_graph, s, t):

    path = bfs(graph, residual_graph, s, t)
    while path != None:
        flow = min(graph.adjacency_list[u][v]['capacidad'] - residual_graph.adjacency_list[u][v]['capacidad'] for u,v in path)
        for u,v in path:
            residual_graph.adjacency_list[u][v]['capacidad'] += flow
            residual_graph.adjacency_list[v][u]['capacidad'] -= flow
        path = bfs(graph, residual_graph, s, t)
    return residual_graph

# find path by using BFS
def bfs(graph, residual, s, t):
    queue = [s]
    paths = {s:[]}
    if s == t:
        return paths[s]
    while queue:
        node = queue.pop(0)
        for (adj, info) in graph.adjacency_list[node].items():
            if(info['capacidad']-residual.adjacency_list[node][adj]['capacidad']>0) and adj not in paths:
                paths[adj] = paths[node]+[(node,adj)]
                if adj == t:
                    return paths[adj]
                queue.append(adj)
    return None

