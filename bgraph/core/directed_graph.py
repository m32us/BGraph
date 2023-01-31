from typing import Optional, Union
from bgraph.core.graph import ABCGraph, ABCEdge, ABCNode
from copy import deepcopy

class DEdge(ABCEdge):
    def __init__(self, direction: str, label: Optional[int] = None, data: Optional[object] = None) -> None:
        super().__init__(label, data)
        if direction in {'in', 'out'}:
            self.direction: str = direction
        else:
            raise KeyError('Node\'s construction fails.')


class DNode(ABCNode):
    def __init__(self, label: Optional[int] = None, data: Optional[object] = None) -> None:
        super().__init__(label, data)
        self.list_edge: list[DEdge] = []

class DBGraph(ABCGraph):
    def __init__(self) -> None:
        super().__init__()
        self.list_node: dict[int, DNode] = {}
        self.is_directed = True

    def add_edge(self, node1: int, node2: int, edge: Optional[DEdge] = None) -> Union[None, KeyError]:
        if edge is None:
            edge_1 = DEdge('out', self.num_edge+1)
            edge_2 = DEdge('in', self.num_edge+1)
        else:
            if edge.direction != 'out':
                raise KeyError(f'The edge must be from node {node1} to node {node2}.')
            edge_1 = edge
            edge_2 = deepcopy(edge)
            edge_2.direction = 'in'

        node_1: Optional[ABCNode] = self.list_node.get(node1)
        node_2: Optional[ABCNode] = self.list_node.get(node2)
        if node_1 is not None and node_2 is not None:
            node_1.list_neighbor.append(node2)
            node_1.list_edge.append(edge_1)
            node_2.list_neighbor.append(node1)
            node_2.list_edge.append(edge_2)
            self.num_edge += 1
        else:
            raise KeyError(f'Can\'t add edge between node {node1} and node {node2}.')

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

    def remove_edge(self, start_node: int, end_node: int, edge_label: Optional[int] = None) -> Union[None, KeyError]:
        node_1: Optional[ABCNode] = self.list_node.get(start_node)
        node_2: Optional[ABCNode] = self.list_node.get(end_node)
        if node_1 is not None and node_2 is not None and start_node in node_2.list_neighbor:
            if edge_label is None:
                self.remove_all_edges(start_node, end_node)
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

    def remove_node(self, node: int) -> Union[None, KeyError]:
        node_ = self.list_node.get(node)
        if node_ is not None:
            for neighbor in node_.list_neighbor:
                self.remove_all_edges(node, neighbor)
            del(self.list_node[node])
            self.num_node -= 1
        else:
            raise KeyError(f'Can\'t remove node {node}.')

    def get_degree(self, node: int, direction: Optional[str]=None) -> Union[int, KeyError]:
        node_ = self.list_node.get(node)
        if node_ is not None and direction in {'in', 'out', None}:
            if direction is None:
                return len(node_.list_edge)
            else:
                count = 0
                for edge in node_.list_edge:
                    if edge.direction == direction:
                        count += 1
                return count
        else:
            raise KeyError(f'Can\'t get the degree of node {node}.')

    def print_adj_list(self) -> None:
        print(f'Num node: {self.num_node}')
        print(f'Num edge: {self.num_edge}')
        for key in self.list_node.keys():
            print(f'{key} ({self.get_degree(key)} = {self.get_degree(key, "in")} + {self.get_degree(key, "out")}): ', end='')
            for idx, neighbor in enumerate(self.list_node[key].list_neighbor):
                if self.list_node[key].list_edge[idx].direction == 'out':
                    print(neighbor, end=' ')
            print()

# graph = DBGraph()

# for i in range(1,7):
#     graph.add_node(DNode(i))

# graph.add_edge(1,2)
# graph.add_edge(3,1)
# graph.add_edge(3,2)
# graph.add_edge(2,4)
# graph.add_edge(4,3)
# graph.add_edge(4,5)
# graph.add_edge(4,6)
# graph.add_edge(6,5)

# graph.print_adj_list()
# print()

# # graph.remove_edge(1,2,69)
# graph.remove_edge(1,4)
# graph.print_adj_list()
# print()
