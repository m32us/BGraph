import abc as abstract
from typing import Optional, Union


class ABCEdge:
    """abstract class for Edge
    """

    def __init__(
        self,
        label: Optional[int] = None,
        data: Optional[object] = None
    ) -> None:
        self.label = label
        self.data = data

    def get_label(self) -> Optional[int]:
        return self.label

    def get_data(self) -> Optional[object]:
        return self.data

    def __repr__(self) -> str:
        return '(label: {}, data: {})'.format(self.get_label(), self.get_data())


class ABCNode:
    """abstract class for Node
    """

    def __init__(
        self,
        label: Optional[int] = None,
        data: Optional[object] = None,
    ) -> None:
        self.data = data
        self.label = label
        self.list_neighbor: list[int] = []  # store label of neighbor nodes
        self.list_edge: list[ABCEdge] = []

    def get_data(self) -> Optional[object]:
        return self.data

    def get_label(self) -> Optional[int]:
        return self.label

    def get_list_neighbor(self) -> list[int]:
        return self.list_neighbor

    def get_list_edge(self) -> list[ABCEdge]:
        return self.list_edge


class ABCGraph:
    """abstract class for Graph
    """

    def __init__(self) -> None:
        self.list_node: dict[int, ABCNode] = {}
        self.num_node = 0
        self.num_edge = 0
        self.is_directed:bool = False

    @abstract.abstractmethod
    def read_graph_from_file(self, file_name: str):
        """read the whole file to generate a graph. assume that this file is small

        Args:
            file_name (str): path to the file
        """
        pass

    @abstract.abstractmethod
    def add_edge(self, node1: int, node2: int, edge: Optional[ABCEdge] = None) -> Union[None, KeyError]:
        """add an edge between 2 node node1 and node2.
        this method will execute differently in directed and undirected graph

        Args:
            node1 (int): label of the first node
            node2 (int): label of the second node
            edge (Optional[ABCEdge], optional): edge info if needed. Defaults to None.
        """
        pass

    def add_node(self, node: ABCNode) -> Union[None, ValueError]:
        """add a node to list_node.
        if node's label is none, gen a new label based on num_node

        Args:
            node (ABCNode): a node

        Returns:
            bool: return True if succeed. False if fail
        """
        # construct node without label
        if node.label is None:
            self.num_node += 1
            self.list_node[self.num_node] = node
        # construct node with label and label is not in list_node
        elif self.list_node.get(node.label) is None:
            self.list_node[node.label] = node
            self.num_node += 1
        else:
            # self.list_node[node.label] = node
            raise ValueError(f'Add node ({node.label}, {node.data}) failed')

    @abstract.abstractmethod
    def remove_node(self, node: int) -> Union[None, KeyError]:
        """remove a node in graph.
        if graph is undirected, just visit all its neighbors and remove the connection
        before remove `node` from `list_node`
        if graph is directed, ???

        Args:
            node (int): label of node

        Returns:
            bool: return True if succeed. False if fail
        """
        pass

    @abstract.abstractmethod
    def remove_edge(self, start_node: int, end_node: int) -> Union[None, KeyError]:
        """remove an edge from start_node to end_node.
        if graph is undirected, we have to remove edge in both start_node and end_node

        Args:
            start_node (int): label of start node
            end_node (int): label of end node

        Returns:
            bool: return True if succeed. False if fail
        """
        pass

    @abstract.abstractmethod
    def get_degree(self, node: int) -> Union[int, KeyError]:
        """calculate the degree of a node

        Args:
            node (int): label of a node

        Returns:
            int: degree of node
        """
        pass
