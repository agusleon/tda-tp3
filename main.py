import argparse
from digraph import Digraph
from max_flow import bfs, max_flow

SOURCE_NAME = "S"
SINK_NAME = "T"
SOURCE_NAME_AUX = "S_aux"
SINK_NAME_AUX = "T_aux"
INF = 10000000

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="El path del archivo red.txt")
    return parser


def load_network(path):
    # Nodo_origen,Nodo_destino,capacidad,demanda
    with open(path, "r") as file:
        result = []
        for line in file:
            result.append(line.strip().split(","))
        return result
    
def make_residual_graph(graph):
    residual = Digraph()
    for (current_node, _) in graph.adjacency_list.items():
        for (node, _) in graph.adjacency_list.items():
            if current_node != node:
                residual.add_edge(node, current_node, 0, 0)
                residual.add_edge(current_node, node, 0, 0)
        residual.add_edge(SINK_NAME_AUX, current_node, 0, 0)
        residual.add_edge(current_node, SINK_NAME_AUX, 0, 0)
    
    return residual

def reduce_graph(graph):

    graph_aux = Digraph()

    for (current_node, current_adjacency) in graph.adjacency_list.items():

        # For each vertex add an edge from new source S' to each vertex with capacity(s', u) = sum(demand(v,u) for each v)
        total_outgoing_demand = 0
        for adj_info in current_adjacency.values():
            total_outgoing_demand += adj_info['demanda']
        graph_aux.add_edge(current_node, SINK_NAME_AUX, total_outgoing_demand, 0)

        # For each vertex add an edge to new sink T' from each vertex with capacity(u, s') = sum(demand(u,v) for each v)
        total_incoming_demand = 0
        for (_, adjacency) in graph.adjacency_list.items():
            if current_node in adjacency:
                total_incoming_demand += adjacency[current_node]['demanda']
        graph_aux.add_edge(SOURCE_NAME_AUX, current_node, total_incoming_demand, 0)

        # For each edge in the old network transform the capacity(u, v) = capacity(u, v) - demand(u, v)
        for (adj, info) in current_adjacency.items():
            graph_aux.add_edge(current_node, adj, info['capacidad'] - info['demanda'], 0)

    # Add an edge from t to s with INFINITE capacity
    graph_aux.add_edge(SINK_NAME, SOURCE_NAME, INF, 0)

    return graph_aux



if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    net = load_network(args.path)
    graph = Digraph()

    for edge in net:
        source_node, destination_node, capacity, demand = edge
        graph.add_edge(source_node, destination_node, capacity=int(capacity), demand=int(demand))
    graph.add_edge(SINK_NAME, None, 0, 0)

    print(graph)

    reduced_graph = reduce_graph(graph)

    print(reduced_graph)


    residual_graph = make_residual_graph(reduced_graph)

    print(residual_graph)
    
    print(max_flow)
    max_flow = max_flow(reduced_graph, residual_graph, SOURCE_NAME_AUX, SINK_NAME_AUX)
    print(max_flow)

    # SIMPLE TEST

    # reduced_graph = Digraph()
    # reduced_graph.add_edge(SOURCE_NAME, 'B', 3, 0)
    # reduced_graph.add_edge(SOURCE_NAME, 'C', 3, 0)
    # reduced_graph.add_edge('B', 'C', 5, 0)
    # reduced_graph.add_edge('B', 'D', 3, 0)
    # reduced_graph.add_edge('C', 'E', 5, 0)
    # reduced_graph.add_edge('D', 'E', 4, 0)
    # reduced_graph.add_edge('D', SINK_NAME, 5, 0)
    # reduced_graph.add_edge('E', SINK_NAME, 5, 0)
    # reduced_graph.add_edge(SINK_NAME, None, 0, 0)

    # max_flow = max_flow(reduced_graph, residual_graph, SOURCE_NAME, SINK_NAME)