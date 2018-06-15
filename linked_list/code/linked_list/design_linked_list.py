# coding: utf-8

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


class MyLinkedList(object):

	def __init__(self):
		self.head = None
		

	"""
	获取链表中 第 index 个节点的值
		如果 index 不合法 返回 None
	: type index : int
	: rtype: int
	"""
	def get(self, index):
		cur = self.head
		cur_index = 0
		
		# 空链表
		if cur is None:
			return None

		# 循环 到 第 index 个节点
		while cur_index < index:
			cur = cur.next
			if cur is None:	# 说明 index 大于 链表的长度
				return None
			cur_index += 1

		return cur.val

	# 头插入 节点
	def addAtHead(self, val):
		node = Node(val)
		cur = self.head

		# 空链表
		if cur is None:
			self.head = node
			return 

		node.next = self.head
		self.head = node

	def addAtTail(self, val):
		node = Node(val)

		cur = self.head

		if cur is None:
			self.head = node
			return

		#遍历至 尾节点 
		while cur.next is not None:
			cur = cur.next

		cur.next = node
		return 

	def addAtIndex(self, index, val):
		node = Node(val)

		cur = self.head
		cur_index = 0
		
		if cur is None:
			# 空链表 插入的 index > 0
			if cur_index < index:
				return False
			# 空链表 index == 0 插入头节点
			if cur_index == index:
				self.head = node
				return


		# 找到 index-1 
		while cur_index < index - 1:
			cur = cur.next
			if cur is None:
				return 
			cur_index += 1

		# 若 index 不为空
		if cur.next is not None:
			node.next = cur.next
		cur.next = node
		return

	def deleteAtIndex(self, index):
		cur = self.head
		cur_index = 0

		# 空链表
		if cur is None:
			return

		while cur_index < index - 1:
			cur = cur.next
			if cur is None:
				return 
			cur_index += 1

		# 找到前一个节点
		if cur.next is None:
			return 
		# 将前一个节点的 next 指向 下一个节点
		cur.next = cur.next.next

	def get(self, index):
		cur = self.head
		cur_index = 0

		# 空链表
		if cur is None:
			return -1

		while cur_index < index:
			cur = cur.next
			if cur is None:
				return -1

			cur_index += 1

		return cur.val

	# 长度操作
	def size(self):
		cur = self.head
		count = 0
		if cur is None:
			return 0
		# 头节点
		count  = 1

		while cur.next is not None:
			cur = cur.next
			count += 1

		return count

	def is_empty(self):
		return self.head is None

	def travel(self):
		cur = self.head
		if cur is None:
			return 
		print(cur.val,"->")
		while cur.next is not None:
			cur = cur.next
			print(cur.val,"->")

	def reverse(self):
		pre = None
		cur = self.head
		while cur is not None:
			next = cur.next
			cur.next = pre

			pre = cur
			cur = next

		self.head = pre



if __name__ == '__main__':

	"""
	["MyLinkedList","get","addAtIndex","get","get","addAtIndex","get","get"]
	[[],[0],[1,2],[0],[1],[0,1],[0],[1]]
	"""
	m = MyLinkedList()
	m.addAtHead(7)
	m.addAtHead(2)
	m.addAtHead(1)
	# m.travel()
	m.addAtIndex(3, 0)
	# m.travel()
	m.deleteAtIndex(2)
	# m.travel()
	m.addAtHead(6)
	# m.travel()
	m.addAtTail(4)
	m.travel()
	m.reverse()
	m.travel()
	print(m.size())
	# print(m.get(0))
	# m.addAtIndex(1, 2)
	# print(m.get(0))
	# print(m.get(1))
	# m.addAtIndex(0, 1)
	# print(m.get(0))
	# print(m.get(1))

	# # m.addAtHead(1)
	# # m.addAtTail(3)
	# m.addAtIndex(1, 2)
	# m.travel()
	# print(m.get(0))
	# print(m.get(1))
	# m.addAtIndex(1, 2)
	# print(m.get(0))
	# print(m.get(1))
	# # m.deleteAtIndex(1)
	# # m.travel()
	# # print(m.get(1))
	# m.travel()


	# 0103211


	# c = 6
	# b = words[-1358026495, -1286471680]




	



	

