# coding: utf-8

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

header_node = Node(12)
node_b = Node(11)
node_c = Node(12)
node_d = Node(13)


header_node.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = None




