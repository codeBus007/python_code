# coding: utf-8

from copy import deepcopy

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def travel(node):
	if node is not None:
		print(node.val)

	while node.next is not None:
		node = node.next
		print(node.val)

	print("*****end******")

class Solution(object):
	@staticmethod
	def deep_copy_linked_list(head):
		if head is None:
			return None


		head2 = deepcopy(head)
		cur = head2

		while head.next is not None:
			cur.next = deepcopy(head.next)

			cur = cur.next
			head = head.next


		return head2


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
travel(a)

w = Solution.deep_copy_linked_list(a)
travel(w)

b.val = 999

travel(a)

travel(w)



			