import abc as abstract
from typing import Optional

class ABCEdge:
    """abstract class for Edge
    """

    def __init__(
        self,
        label:Optional[int]=None,
        data:Optional[object]=None
    ) -> None:
        self.label = label
        self.data = data

class ABCNode:
    """abstract class for Node
    """

    def __init__(
        self,
        label:Optional[int]=None,
        data:Optional[object]=None,
    ) -> None:
        self.data = data
        self.label = label
        self.list_neighbor:list[int] = [] # store label of neighbor nodes
        self.list_edge:list[ABCEdge] = []

class ABCGraph:
    """abstract class for Graph
    """

    def __init__(
        self,
        num_node:int=0,
        num_edge:int=0
    ) -> None:
        self.list_node:dict[int,ABCNode] = {}
        self.num_node = num_node
        self.num_edge = num_edge

    @abstract.abstractmethod
    def add_edge(self, node1:int, node2:int, edge:Optional[ABCEdge]=None):
        """add an edge between 2 node node1 and node2.
        this method will execute differently in directed and undirected graph

        Args:
            node1 (int): label of the first node
            node2 (int): label of the second node
            edge (Optional[ABCEdge], optional): edge info if needed. Defaults to None.
        """
        pass

    def add_node(self, node:ABCNode)->bool:
        """add a node to list_node. 
        if node's label is none, gen a new label based on num_node

        Args:
            node (ABCNode): a node

        Returns:
            bool: return True if succeed. False if fail
        """
        if node.label is None:
            self.num_node += 1
            self.list_node[self.num_node] = node
            return True
        elif self.list_node.get(node.label) is None:
            self.list_node[node.label] = node
            self.num_node += 1
            return True
        else:
            # self.list_node[node.label] = node
            return False

    @abstract.abstractmethod
    def remove_node(self, node:int)->bool:
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
    def remove_edge(self, start_node:int, end_node:int)->bool:
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
    def get_degree(self, node:int)->int:
        """calculate the degree of a node

        Args:
            node (int): label of a node

        Returns:
            int: degree of node
        """
        pass
