# coding: utf-8
from node_defined import Node, header_node
from travel_singly_linked_list import travel

# 将 1000 的Node 插入到 12的Node 之前

node_new = Node(1000)

# 
# 返回 -1 头节点还是原来的头节点 返回1 头节点变成插入的节点
def add(inserted_node, header_node):
	if header_node.next.val == 12:
		inserted_node.next = header_node.next
		header_node.next = inserted_node
		return
	# 头节点的时候直接插入
	if header_node.val == 12:
		inserted_node.next = header_node
		return
	if header_node.next is not None:
		add(inserted_node, header_node.next)

add(node_new, header_node)
travel(header_node)
travel(node_new)





