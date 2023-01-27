from bgraph.core import ABCGraph, ABCVertex, ABCEdge

class UDBGraph(ABCGraph):
    def __init__(self, num_vertices, is_directed=False):
        super().__init__(num_vertices, is_directed)

    def add_vertex(self, vertex: ABCVertex):
        return super().add_vertex(vertex)

    def add_egde(self, edge: ABCEdge, weight=0):
        return super().add_egde(edge, weight)

    def remove_vertex(self, vertex: ABCVertex):
        return super().remove_vertex(vertex)

    def remove_edge(self, edge: ABCEdge):
        return super().remove_edge(edge)

    def get_adjacent_vertices(self, vertex: ABCVertex):
        return super().get_adjacent_vertices(vertex)

    def get_indegree(self, vertex: ABCVertex):
        return super().get_indegree(vertex)

    def get_outdegree(self, vertex: ABCVertex):
        return super().get_outdegree(vertex)

    def get_adjacent_vertices(self, vertex: ABCVertex):
        return super().get_adjacent_vertices(vertex)

    def adjacency_list(self):
        return super().adjacency_list()

    def adjacency_list(self):
        return super().adjacency_list()


