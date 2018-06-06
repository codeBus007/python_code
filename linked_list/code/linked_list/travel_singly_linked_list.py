# coding:utf-8

from node_defined import header_node, node_b, node_c, node_d


def travel(node):
	print(node.val)
	if node.next is not None:
		travel(node.next)



# travel(header_node)