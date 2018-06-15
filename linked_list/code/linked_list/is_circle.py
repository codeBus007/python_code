# coding: utf-8

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):
	def __init__(self, head):
		self.faster = head
		self.slower = head

	def has_circle(self):
		if self.faster:
			self.faster = self.faster.next
			self.slower = self.slower.next

			while self.faster:
				self.faster = self.faster.next
				self.slower = self.slower.next
				if self.faster:
					self.faster = self.faster.next

					if self.faster is self.slower:
						return True

		return False





a_node = Node(2)
b_node = Node(3)
c_node = Node(3)
d_node = Node(3)
e_node = Node(3)
f_node = Node(3)
g_node = Node(3)


a_node.next = b_node
b_node.next = c_node
c_node.next = d_node
d_node.next = e_node
e_node.next = f_node
f_node.next = g_node

# circle 
# g_node.next = d_node

s = Solution(a_node)

print(s.has_circle())








