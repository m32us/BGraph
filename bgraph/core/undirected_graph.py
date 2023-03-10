from bgraph.core import ABCNode, ABCEdge, ABCGraph

from typing import Optional, Union

# from bgraph.utils.fileio import getline, get_adjacency_list, get_node_info, buf_count_newlines_gen


class UDBGraph(ABCGraph):
    def __init__(self, data_path: Optional[str] = None) -> None:
        ABCGraph.__init__(self)
        # if data_path is not None:
        #     self.data_path = data_path
        #     try:
        #         is_directed, self.num_node, self.num_edge, self.list_node = self.read_graph_from_file(
        #             data_path=data_path)
        #     except Exception as err:
        #         raise err

    # def read_graph_from_file(self, data_path: str):
    #     lst_nodes = {}
    #     num_edges = 0

    #     num_nodes = buf_count_newlines_gen(data_path + '/vertices_lst')
    #     is_directed = (False, True)[getline(
    #         data_path + '/vertices_lst', 1) == 'D']

    #     for i in range(num_nodes):
    #         label, data = get_node_info(i+2, data_path)
    #         list_neighbor, label_lst, data_lst = get_adjacency_list(
    #             i+1, data_path)
    #         lst_nodes[i] = ABCNode(label=label, data=data)
    #         lst_nodes[i].list_neighbor = list_neighbor
    #         lst_nodes[i].list_edge = [
    #             ABCEdge(label=l, data=d) for l, d in zip(label_lst, data_lst)]

    #         num_edges += len(lst_nodes[i].list_edge)

    #     return is_directed, num_nodes, num_edges, lst_nodes

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
        return self.list_node.get(label) is not None
        # for key, value in self.list_node.items():
        #     if value.get_label() == label:
        #         return True
        # return False

    # def add_node(self, node: ABCNode) -> bool:
    #     if not self.__check_exist_label(node.get_label()):
    #         self.num_node += 1
    #         self.list_node[self.num_node] = node
    #     else:
    #         raise UserWarning('Node has already existed in graph.')
    #     return True

    def add_edge(self, node1: int, node2: int, edge: Optional[ABCEdge] = None) -> Union[None, KeyError]:
        if edge is None:
            edge = ABCEdge(self.num_edge+1)

        node_1: Optional[ABCNode] = self.list_node.get(node1)
        node_2: Optional[ABCNode] = self.list_node.get(node2)
        if node_1 is not None and node_2 is not None:
            node_1.list_neighbor.append(node2)
            node_1.list_edge.append(edge)
            node_2.list_neighbor.append(node1)
            node_2.list_edge.append(edge)
            self.num_edge += 1
        else:
            raise KeyError(f'Can\'t add edge between node {node1} and node {node2}.')


    # def add_edge(self, node1: int, node2: int, edge: Optional[ABCEdge] = None):
    #     # Ki???m tra index node1 c?? n???m trong list node hay kh??ng?
    #     if not self.__check_exist_label(node1):
    #         self.add_node(ABCNode(label=node1))

    #     # Ki???m tra index node2 c?? n???m trong list node hay kh??ng?
    #     if not self.__check_exist_label(node2):
    #         self.add_node(ABCNode(label=node2))

    #     # Th??m node2 v??o list_neighbor c???a node1
    #     self.list_node[node1].list_neighbor.append(node2)

    #     # Th??m node1 v??o list_neighbor c???a node2
    #     self.list_node[node2].list_neighbor.append(node1)

    #     # N???u th??ng tin v??? c???nh l?? c??
    #     if edge is not None:
    #         # Th??m v??o list_edge c???a node1
    #         self.list_node[node1].list_edge.append(
    #             ABCEdge(label=edge.label, data=edge.data))

    #         # Th??m v??o list_edge c???a node2
    #         self.list_node[node2].list_edge.append(
    #             ABCEdge(label=edge.label, data=edge.data))

    # def remove_node(self, node: int) -> Union[None, KeyError]:
    #     # Ki???m tra xem node c???n x??a c?? t???n t???i trong ????? th??? hay kh??ng?
    #     if not self.__check_exist_label(node):
    #         raise KeyError(f'Can\'t remove node {node}.')

    #     # N???u c?? t???n t???i, th?? chu???n b??? x??a n??
    #     # B?????c 1: X??a c??c li??n k???t v???i n??t c???n x??a
    #     for key, value in self.list_node.items():
    #         if key != node:
    #             # T??m list indices ????? x??a
    #             del_indices = [i for i in range(
    #                 len(value.list_neighbor)) if value.list_neighbor[i] == node]

    #             # X??a trong list neighbor
    #             value.list_neighbor = [value.list_neighbor[k] for k, v in enumerate(
    #                 value.list_neighbor) if k not in del_indices]

    #             # X??a trong list edge
    #             value.list_edge = [value.list_edge[k] for k, v in enumerate(
    #                 value.list_edge) if k not in del_indices]

    #     # B?????c 2: X??a n??t c???n x??a
    #     try:
    #         del self.list_node[node]
    #     except UserWarning('Error when delete node in graph.') as usr_warning:
    #         return usr_warning

    # def remove_edge(self, start_node: int, end_node: int) -> bool:
    #     # Ki???m tra node start c?? n???m trong graph hay kh??ng?
    #     # N???u kh??ng th?? th??i, j c??ng
    #     if not self.__check_exist_label(start_node):
    #         raise UserWarning('Start node does not exist in graph.')

    #     # Ki???m tra end start c?? n???m trong graph hay kh??ng?
    #     # N???u kh??ng th?? th??i, j c??ng
    #     if not self.__check_exist_label(end_node):
    #         raise UserWarning('End node does not exist in graph.')

    #     # V??o ki???m tra danh s??ch k???, danh s??ch c???nh c???a n??t start_node
    #     if end_node in self.list_node[start_node].list_neighbor:
    #         del_indices = [i for i in range(len(
    #             self.list_node[start_node].list_neighbor)) if self.list_node[start_node].list_neighbor[i] == end_node]
    #         self.list_node[start_node].list_neighbor = [self.list_node[start_node].list_neighbor[k]
    #                                                     for k, v in enumerate(self.list_node[start_node].list_neighbor) if k not in del_indices]
    #         self.list_node[start_node].list_edge = [self.list_node[start_node].list_edge[k]
    #                                                 for k, v in enumerate(self.list_node[start_node].list_edge) if k not in del_indices]
    #     else:
    #         raise UserWarning('Start node doesn\'t connect with end node.')

    #     # V??o ki???m tra danh s??ch k???, danh s??ch c???nh c???a n??t start_node
    #     if start_node in self.list_node[end_node].list_neighbor:
    #         del_indices = [i for i in range(len(
    #             self.list_node[end_node].list_neighbor)) if self.list_node[end_node].list_neighbor[i] == start_node]
    #         self.list_node[end_node].list_neighbor = [self.list_node[end_node].list_neighbor[k]
    #                                                   for k, v in enumerate(self.list_node[end_node].list_neighbor) if k not in del_indices]
    #         self.list_node[end_node].list_edge = [self.list_node[end_node].list_edge[k]
    #                                               for k, v in enumerate(self.list_node[end_node].list_edge) if k not in del_indices]
    #     else:
    #         raise UserWarning('End node doesn\'t connect with start node.')

    def get_indegree(self, node: int) -> Union[int, Exception]:
        """Get indegree of input node

        Args:
            node (int): Input node label that need to be calculated its indegree.

        Returns:
            Union[int, Exception]: Return Integer number that represents its indegree. Otherwise, return Exception for raising error notifications.
        """
        try:
            in_deg = self.get_degree(node=node)
        except UserWarning('Error occurs.') as usr_warning:
            return usr_warning
        return in_deg

    def get_outdegree(self, node: int) -> Union[int, Exception]:
        """Get outdegree of input node

        Args:
            node (int): Input node label that need to be calculated its outdegree.

        Returns:
            Union[int, Exception]: Return Integer number that represents its outdegree. Otherwise, return Exception for raising error notifications.
        """
        try:
            out_deg = self.get_degree(node=node)
        except UserWarning('Error occurs.') as usr_warning:
            return usr_warning
        return out_deg

    def get_degree(self, node: int) -> Union[int, Exception]:
        """Get degree of input node

        Args:
            node (int): Input node label that need to be calculated its degree.

        Returns:
            Union[int, Exception]: Return Integer number that represents its degree. Otherwise, return Exception for raising error notifications.
        """
        try:
            deg = len(self.list_node[node].list_neighbor)
        except UserWarning('Error occurs.') as usr_warning:
            return usr_warning
        return deg

    def node_induced_subgraph(self, induced_lst_nodes: list[int]) -> Union[bool, ResourceWarning]:
        """Induced subgraph based on induced nodes

        A node-induced subgraph is a graph with edges whose endpoints are both in the specified node set.

        Return a subgraph induced on the given nodes.

        Args:
            induced_lst_nodes (list[int]): The nodes to form the subgraph. Listing of integer label.

        Returns:
            Union[bool, ResourceWarning]:
        """
        for node in induced_lst_nodes:
            try:
                if not self.__check_exist_label(node): raise
            except ResourceWarning('Input induced list node has element that not exist in graph.') as res_warning:
                return res_warning

        result_lst_nodes = dict()

        for node in induced_lst_nodes:
            target = node
            # print(target)
            # print(self.list_node[node].list_neighbor)
            rest = [x for x in induced_lst_nodes if x != node]
            lst_neighbor = [(int(x), y) for x, y in zip(self.list_node[node].list_neighbor, self.list_node[node].list_edge) if int(x) in rest]

            result_lst_nodes[target] = lst_neighbor

        # print for debug
        for key, value in result_lst_nodes.items():
            print(key)
            print(value)

        # save, dump ccj ???? v???i c??i l??y
        # ...

    def edges_induced_subgraph(self, induced_lst_edges: list[int]) -> Union[bool, ResourceWarning]:
        """Induced subgraph based on induced edges.

        An edge-induced subgraph is equivalent to creating a new graph using the given edges

        Return a subgraph induced on the given edges.

        Args:
            induced_lst_edges (list[int]): The edges to form the subgraph.

        Returns:
            Union[bool, ResourceWarning]:
        """
        pass
