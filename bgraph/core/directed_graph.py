from bgraph.core import ABCGraph, ABCVertex, ABCEdge

class DBGraph(ABCGraph):
    def __init__(self, num_vertices):
        super().__init__(num_vertices, True)

    def add_vertex(self, vertex: ABCVertex):
        return super().add_vertex(vertex)

    