class Digraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination, capacity, demand):
        if source in self.adjacency_list:
            self.adjacency_list[source][destination] = {"capacidad":capacity, "demanda":demand}
        else:
            if destination is None:
                self.adjacency_list[source] = {}
            else:
                self.adjacency_list[source] = {destination:{"capacidad":capacity, "demanda":demand}}
    
    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return []

    def has_edge(self, source, destination):
        if source in self.adjacency_list:
            return destination in self.adjacency_list[source]
        else:
            return False

    def __str__(self):
        graph_str = ""
        for vertex in self.adjacency_list:
            neighbors = self.adjacency_list[vertex]
            print(vertex," -> ",neighbors)
        return graph_str
