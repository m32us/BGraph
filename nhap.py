from typing import Optional, Union
from bgraph.utils import read_graph_from_file

graph = read_graph_from_file('./node.txt', './adj_list.txt')
list_node = graph.list_node
node1 = list_node[1]
list_edge1 = node1.list_edge
for item in list_edge1:
    print(item.data)

"""
# hàm đọc đồ thị từ file (đọc nguyên cái file)
# viết tại `./bgraph/core/` cho đồ thị có hướng (vô hướng đã viết bởi nam)
    - input là filename, output là object đồ thị
    - check kích thước của file
    - khởi tạo 1 đồ thị ABCGraph
    - viết hàm đọc 1node của đồ thị `read_node_from_file(filename, line_number)->ABCNode`. sau khi đọc xong node nghĩa là đã có danh sách kề các thứ rồi.
    - Add con node vừa đọc được vào đồ thị vừa khởi tạo

# hàm trích đồ thị con từ file (đọc các dòng xác đinh trong file)
# viết tại `./bgraph/algorithms`
    - input là filename, list_node:list[int] các label node cần rút trích, output là object đồ thị
    - nếu đọc tới dòng nào mà k có data thì raise lỗi
    - tạo con đồ thị
    - đọc dòng tới đâu trả ra node để add vào đồ thị tới đó. lúc vừa lấy được con node (gọi hàm `read_node_from_file`) thì chỉnh sửa lại danh sách kề và danh sách cạnh của node đó rồi thêm vào đồ thị
"""
