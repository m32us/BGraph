from bgraph.core import ABCNode, ABCEdge, ABCGraph

from typing import Optional, Union

from bgraph.utils.fileio import opt_get_number_of_nodes, opt_get_number_of_edges, get_adjacency_list, get_node_info


class UDBGraph(ABCGraph):
    def __init__(self, data_path: Optional[str] = None) -> None:
        ABCGraph.__init__(self)
        if data_path is not None:
            self.data_path = data_path
            try:
                self.num_node, self.num_edge, self.list_node = self.read_graph_from_file(
                    file_name=data_path)
            except:
                raise UserWarning('Filename is not found.')

    def read_graph_from_file(self, file_name: str):
        try:
            num_node = opt_get_number_of_nodes(file_path=file_name)
            num_edge = opt_get_number_of_edges(file_path=file_name)
        except:
            raise UserWarning('Filename is not found.')

        lst_nodes = {}
        for i in range(num_node):
            label, data = get_node_info(i+1, file_name)
            list_neighbor, label_lst, data_lst = get_adjacency_list(
                i+1, file_name)
            lst_nodes[i] = ABCNode(label=label, data=data)
            lst_nodes[i].list_neighbor = list_neighbor
            lst_nodes[i].list_edge = [
                ABCEdge(label=l, data=d) for l, d in zip(label_lst, data_lst)]
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

    # def add_node(self, node: ABCNode) -> bool:
    #     if not self.__check_exist_label(node.get_label()):
    #         self.num_node += 1
    #         self.list_node[self.num_node] = node
    #     else:
    #         raise UserWarning('Node has already existed in graph.')
    #     return True

    def add_edge(self, node1: int, node2: int, edge: Optional[ABCEdge] = None):
        # Kiểm tra index node1 có nằm trong list node hay không?
        if not self.__check_exist_label(node1):
            self.add_node(ABCNode(label=node1))

        # Kiểm tra index node2 có nằm trong list node hay không?
        if not self.__check_exist_label(node2):
            self.add_node(ABCNode(label=node2))

        # Thêm node2 vào list_neighbor của node1
        self.list_node[node1].list_neighbor.append(node2)

        # Thêm node1 vào list_neighbor của node2
        self.list_node[node2].list_neighbor.append(node1)

        # Nếu thông tin về cạnh là có
        if edge is not None:
            # Thêm vào list_edge của node1
            self.list_node[node1].list_edge.append(
                ABCEdge(label=edge.label, data=edge.data))

            # Thêm vào list_edge của node2
            self.list_node[node2].list_edge.append(
                ABCEdge(label=edge.label, data=edge.data))

    def remove_node(self, node: int) -> Exception:
        # Kiểm tra xem node cần xóa có tồn tại trong đồ thị hay không?
        try:
            if not self.__check_exist_label(node):
                raise  # Nếu không thì thôi, j căng
        except UserWarning('Node does not exist in graph.') as usr_warning:
            return usr_warning

        # Nếu có tồn tại, thì chuẩn bị xóa nó
        else:
            # Bước 1: Xóa các liên kết với nút cần xóa
            for key, value in self.list_node.items():
                if key != node:
                    # Tìm list indices để xóa
                    del_indices = [i for i in range(
                        len(value.list_neighbor)) if value.list_neighbor[i] == node]

                    # Xóa trong list neighbor
                    value.list_neighbor = [value.list_neighbor[k] for k, v in enumerate(
                        value.list_neighbor) if k not in del_indices]

                    # Xóa trong list edge
                    value.list_edge = [value.list_edge[k] for k, v in enumerate(
                        value.list_edge) if k not in del_indices]

            # Bước 2: Xóa nút cần xóa
            try:
                del self.list_node[node]
            except UserWarning('Error when delete node in graph.') as usr_warning:
                return usr_warning

    def remove_edge(self, start_node: int, end_node: int) -> bool:
        # Kiểm tra node start có nằm trong graph hay không?
        # Nếu không thì thôi, j căng
        if not self.__check_exist_label(start_node):
            raise UserWarning('Start node does not exist in graph.')

        # Kiểm tra end start có nằm trong graph hay không?
        # Nếu không thì thôi, j căng
        if not self.__check_exist_label(end_node):
            raise UserWarning('End node does not exist in graph.')

        # Vào kiểm tra danh sách kề, danh sách cạnh của nút start_node
        if end_node in self.list_node[start_node].list_neighbor:
            del_indices = [i for i in range(len(
                self.list_node[start_node].list_neighbor)) if self.list_node[start_node].list_neighbor[i] == end_node]
            self.list_node[start_node].list_neighbor = [self.list_node[start_node].list_neighbor[k]
                                                        for k, v in enumerate(self.list_node[start_node].list_neighbor) if k not in del_indices]
            self.list_node[start_node].list_edge = [self.list_node[start_node].list_edge[k]
                                                    for k, v in enumerate(self.list_node[start_node].list_edge) if k not in del_indices]
        else:
            raise UserWarning('Start node doesnot connect with end node.')

        # Vào kiểm tra danh sách kề, danh sách cạnh của nút start_node
        if start_node in self.list_node[end_node].list_neighbor:
            del_indices = [i for i in range(len(
                self.list_node[end_node].list_neighbor)) if self.list_node[end_node].list_neighbor[i] == start_node]
            self.list_node[end_node].list_neighbor = [self.list_node[end_node].list_neighbor[k]
                                                      for k, v in enumerate(self.list_node[end_node].list_neighbor) if k not in del_indices]
            self.list_node[end_node].list_edge = [self.list_node[end_node].list_edge[k]
                                                  for k, v in enumerate(self.list_node[end_node].list_edge) if k not in del_indices]
        else:
            raise UserWarning('End node doesnot connect with start node.')

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
