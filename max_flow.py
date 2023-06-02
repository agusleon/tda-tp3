from digraph import Digraph

#Edmonds-Karp Algorithm
def max_flow(graph, residual_graph, s, t):

    path = bfs(graph, residual_graph, s, t)
    #  print path
    while path != None:
        flow = min(graph.adjacency_list[u][v]['capacidad'] - residual_graph.adjacency_list[u][v]['capacidad'] for u,v in path)
        print(flow)
        for u,v in path:
            residual_graph.adjacency_list[u][v]['capacidad'] += flow
            residual_graph.adjacency_list[v][u]['capacidad'] -= flow
        path = bfs(graph, residual_graph, s, t)
    print("Final graph: ", residual_graph)
    # return sum(residual_graph[s][i] for i in range(n))

# find path by using BFS
def bfs(graph, residual, s, t):
    queue = [s]
    paths = {s:[]}
    if s == t:
        return paths[s]
    while queue: 
        print(queue)
        node = queue.pop(0)
        for (adj, info) in graph.adjacency_list[node].items():
            if(info['capacidad']-residual.adjacency_list[node][adj]['capacidad']>0) and adj not in paths:
                paths[adj] = paths[node]+[(node,adj)]
                print(paths)
                if adj == t:
                    return paths[adj]
                queue.append(adj)
    return None
    
# # make a capacity graph
# # node   s   o   p   q   r   t
# C = [[ 0, 3, 3, 0, 0, 0 ],  # s
#      [ 0, 0, 2, 3, 0, 0 ],  # o
#      [ 0, 0, 0, 0, 2, 0 ],  # p
#      [ 0, 0, 0, 0, 4, 2 ],  # q
#      [ 0, 0, 0, 0, 0, 2 ],  # r
#      [ 0, 0, 0, 0, 0, 0 ]]  # t

# source = 0  # A
# sink = 5    # F
# max_flow_value = max_flow(C, source, sink)
# print("Edmonds-Karp algorithm")
# print("max_flow_value is: ", max_flow_value)

