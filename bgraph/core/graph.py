from interfaces import ABCVertex, ABCEdge, ABCGraph

class Graph(ABCGraph):
    def __init__(self, num_vertices, is_directed=False):
        super().__init__(num_vertices, is_directed)