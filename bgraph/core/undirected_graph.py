from bgraph.core import ABCNode, ABCEdge, ABCGraph

from typing import Optional

from bgraph.utils.fileio import opt_get_number_of_nodes, opt_get_number_of_edges, get_adjacency_list, get_node_info

class UDBGraph(ABCGraph):
    def __init__(self, data_path: Optional[str]=None) -> None:
        ABCGraph.__init__(self)
        if data_path is not None:
            self.data_path = data_path
            try:
                self.num_node, self.num_edge, self.list_node = self.read_graph_from_file(file_name=data_path)
            except:
                raise UserWarning('Filename is not found.')

    def read_graph_from_file(self, file_name: str):
        try:
            num_node = opt_get_number_of_nodes(file_path=file_name)
            num_edge = opt_get_number_of_edges(file_path=file_name)
        except:
            raise UserWarning('Filename is not found.')

        lst_nodes = {}
        for i in range(1, num_node+1):
            label, data = get_node_info(i, file_name)
            list_neighbor, label_lst, data_lst = get_adjacency_list(i, file_name)
            lst_nodes[i] = ABCNode(label=label, data=data)
            lst_nodes[i].list_neighbor = list_neighbor
            lst_nodes[i].list_edge = [ABCEdge(label=l, data=d) for l, d in zip(label_lst, data_lst)]
        return num_node, num_edge, lst_nodes

    def get_num_nodes(self) -> int:
        return self.num_node

    def get_num_edges(self) -> int:
        return self.num_edge

    def get_list_nodes(self):
        # print(type(self.list_node))
        # for key, value in self.list_node.items():
        #     print(key)
        #     print(value.get_label())
        #     print(value.get_list_edge())
        return self.list_node

    def __check_exist_label(self, label: int) -> bool:
        for key, value in self.list_node.items():
            if value.get_label() == label:
                return True
        return False

    def add_node(self, node: ABCNode) -> bool:
        if not self.__check_exist_label(node.get_label()):
            self.num_node += 1
            self.list_node[self.num_node] = node
        else:
            raise UserWarning('Node has already existed in graph.')
        return True

    def add_edge(self, node1: int, node2: int, edge: Optional[ABCEdge] = None):
        if not self.__check_exist_label(node1):
            self.add_node(ABCNode(label=node1))
        if not self.__check_exist_label(node2):
            self.add_node(ABCNode(label=node2))

        self.list_node[node1].list_neighbor.append(node2)
        self.list_node[node2].list_neighbor.append(node1)

        if edge is not None:
            self.list_node[node1].list_edge.append(ABCEdge(label=edge.label, data=edge.data))
            self.list_node[node2].list_edge.append(ABCEdge(label=edge.label, data=edge.data))
        

    def remove_node(self, node: int) -> bool:
        return super().remove_node(node)

    def remove_edge(self, start_node: int, end_node: int) -> bool:
        return super().remove_edge(start_node, end_node)

    def get_degree(self, node: int) -> int:
        return super().get_degree(node)



