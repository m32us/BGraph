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

    def remove_all_edges(self, node1: int, node2: int) -> Union[None, KeyError]:
        node_1: Optional[ABCNode] = self.list_node.get(node1)
        node_2: Optional[ABCNode] = self.list_node.get(node2)
        if node_1 is not None and node_2 is not None:
            # remove node_2 out of list_neighbor and list_edge of node_1
            tmp = list(zip(*[[a, b] for a, b in zip(node_1.list_neighbor, node_1.list_edge) if a != node2]))
            if len(tmp) == 0:
                num_removed_edge = len(node_1.list_edge)
                node_1.list_edge = []
                node_1.list_neighbor = []
            else:
                num_removed_edge = len(node_1.list_edge) - len(tmp[0])
                node_1.list_neighbor = list(tmp[0])
                node_1.list_edge = list(tmp[1])
            self.num_edge -= num_removed_edge

            # remove node_1 out of list_neighbor and list_edge of node_2
            tmp = list(zip(*[[a, b] for a, b in zip(node_2.list_neighbor, node_2.list_edge) if a != node1]))
            if len(tmp) == 0:
                node_2.list_neighbor = []
                node_2.list_edge = []
            else:
                node_2.list_neighbor = list(tmp[0])
                node_2.list_edge = list(tmp[1])
        else:
            raise KeyError(f'Can\'t remove all edges between node {node1} and node {node2}.')

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
            raise ValueError(f'Add node ({node.label}, {node.data}) failed')

    # @abstract.abstractmethod
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
        # pass
        node_ = self.list_node.get(node)
        if node_ is not None:
            for neighbor in node_.list_neighbor:
                self.remove_all_edges(node, neighbor)
            del(self.list_node[node])
            self.num_node -= 1
        else:
            raise KeyError(f'Can\'t remove node {node}.')

    # @abstract.abstractmethod
    def remove_edge(self, start_node: int, end_node: int, edge_label: Optional[int] = None) -> Union[None, KeyError]:
        """remove an edge from start_node to end_node.
        if graph is undirected, we have to remove edge in both start_node and end_node

        Args:
            start_node (int): label of start node
            end_node (int): label of end node

        Returns:
            bool: return True if succeed. False if fail
        """
        # pass
        node_1: Optional[ABCNode] = self.list_node.get(start_node)
        node_2: Optional[ABCNode] = self.list_node.get(end_node)
        if node_1 is not None and node_2 is not None and start_node in node_2.list_neighbor:
            if edge_label is None:
                self.remove_all_edges(start_node, end_node)
                # super().remove_all_edges(start_node, end_node)
            else:
                is_existed_edge_label = False
                # remove edge_label from list_edge of node_1
                for idx, edge in enumerate(node_1.list_edge):
                    if edge.label == edge_label:
                        node_1.list_neighbor.pop(idx)
                        node_1.list_edge.remove(edge)
                        is_existed_edge_label = True
                        self.num_edge -= 1
                        break

                # remove edge_label from list_edge of node_2
                for idx, edge in enumerate(node_2.list_edge):
                    if edge.label == edge_label:
                        node_2.list_neighbor.pop(idx)
                        node_2.list_edge.remove(edge)
                        break

                if not is_existed_edge_label:
                    raise KeyError(f'Can\'t remove edge {edge_label} between node {start_node} and node {end_node}.')
        else:
            raise KeyError(f'Can\'t remove edge between node {start_node} and node {end_node}.')

    @abstract.abstractmethod
    def get_degree(self, node: int) -> Union[int, KeyError]:
        """calculate the degree of a node

        Args:
            node (int): label of a node

        Returns:
            int: degree of node
        """
        pass
