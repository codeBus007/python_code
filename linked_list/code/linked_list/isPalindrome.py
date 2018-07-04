# coding: utf-8

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		super(Node, self).__init__()
		self.val = val
		self.next = None

def isPalindrome(head):
	if head is None or head.next is None:
		return True

	middle = _find_middle(head)
	p, q = head, _reverse_list(middle.next)

	while q is not None:
		if p.val != q.val:
			return False

		p, q = p.next, q.next
	return True

def _find_middle(head):
	slower, faster = head, head.next

	while faster is not None and faster.next is not None:
		slower = slower.next
		faster = faster.next.next

	return slower

def _reverse_list(node):
	pre = None

	while node is not None:
		next = node.next
		node.next = pre
		pre = node
		node = next

	return pre

def gen_list(n, li=None):
	head = Node
	pre = None
	for i in range(n):
		node = Node(i) if li is None else Node(li[i])
		if i == 0:
			head = node
			pre = node
		else:
			pre.next = node
			pre = node

	return head

def travel(node):
	while node is not None:
		print(node.val)
		node = node.next


if __name__ == '__main__':
	head = gen_list(4,[2,1,1,2])
	travel(head)
	print(_find_middle(head).val)
	print(isPalindrome(head))




