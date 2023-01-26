import abc as abstract


class ABCVertex(abstract.ABC):
    """Abstract class for Vertex of the Graph
    """
    def __init__(self, vertex: int, label: str):
        """

        Args:
            vertex (int): _description_
            label (str): _description_
        """
        self.vertex = vertex
        self.label = label

    def get_vertex(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.vertex

    def get_label(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.label


class ABCEdge:
    """Abstract class for Edge of the Graph
    """
    def __init__(self, from_vertex:  ABCVertex, to_vertex:  ABCVertex, label: str, weight=0, is_directed=False):
        """Initialization method

        Args:
            from_vertex (ABCVertex): The first vertex of the edge.
            to_vertex (ABCVertex): The second vertex of the edge.
            label (str): The label of the edge.
            weight (int, optional): The weight of the edge. Defaults to 0.
            is_directed (bool, optional): True if edge is directed, otherwise False. Defaults to False.
        """
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.label = label
        self.weight = weight
        self.is_directed = is_directed

    def get_from_vertex(self):
        """Get the first vertex of the edge

        Returns:
            (ABCVertex): _description_
        """
        return self.from_vertex

    def get_to_vertex(self):
        """Get the second vertex of the edge

        Returns:
            (ABCVertex): _description_
        """
        return self.to_vertex

    def get_weight(self):
        """Get the weight of the edge

        Returns:
            (int) : _description_
        """
        return self.weight

    def get_label(self):
        """Get the label of the edge

        Returns:
            (String): _description_
        """
        return self.label

    def check_directed(self):
        """Check if edge is directed

        Returns:
            (Boolean): _description_
        """
        return self.is_directed

    def __repr__(self):
        """Get the representation of the edge

        Returns:
            _type_: _description_
        """
        return '{}({}, {}, {})'.format(self.__class__.__name__, self.from_vertex, self.to_vertex, self.weight)


class ABCGraph(abstract.ABC):
    """Abstract class for Graph
    """
    def __init__(self, num_vertices, is_directed=False):
        """Initialization method

        Args:
            num_vertices (_type_): _description_
            is_directed (bool, optional): _description_. Defaults to False.
        """
        self.num_vertices = num_vertices
        self.is_directed = is_directed

    @abstract.abstractmethod
    def add_egde(self, edge: ABCEdge, weight=0):
        """Add edge to graph with input weight

        Args:
            edge (ABCEdge): _description_
            weight (int, optional): If graph is weighted graph, this number represents weight of edge {v1, v2}. Defaults to 0.
        """
        pass

    @abstract.abstractmethod
    def add_vertex(self, vertex: ABCVertex):
        """Add vertex to graph

        Args:
            vertex (ABCVertex): _description_
        """
        pass

    @abstract.abstractmethod
    def remove_vertex(self, vertex: ABCVertex):
        """Remove vertex from graph

        Args:
            vertex (ABCVertex): _description_
        """
        pass

    @abstract.abstractmethod
    def remove_edge(self, edge: ABCEdge):
        """Remove edge from graph

        Args:
            edge (ABCEdge): _description_
        """

    @abstract.abstractmethod
    def get_adjacent_vertices(self, vertex: ABCVertex):
        """Get adjacent vertices of input vertex

        Args:
            vertex (ABCVertex): _description_
        """

    @abstract.abstractmethod
    def get_indegree(self, vertex: ABCVertex):
        """Get indegree of input vertex

        Args:
            vertex (ABCVertex): _description_
        """
        pass

    @abstract.abstractmethod
    def get_outdegree(self, vertex: ABCVertex):
        """Get outdegree of input vertex

        Args:
            vertex (ABCVertex): _description_
        """

    @abstract.abstractmethod
    def adjacency_matrix(self):
        """Get adjacency matrix representation of graph
        """
        pass

    @abstract.abstractmethod
    def adjacency_list(self):
        """Get adjacency list representation of graph
        """
        pass

