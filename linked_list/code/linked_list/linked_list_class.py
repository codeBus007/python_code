# coding: utf-8

# 定义节点类 数据域 与 指针域
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	# 判断链表是否为空
	def is_empty(self):
		return self.head is None

	# 追加节点
	def append(self, data):
		node = Node(data)

		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	# 迭代节点
	def iter(self):
		if not self.head:
			return

		cur = self.head
		yield cur.data
		while cur.next:
			cur = cur.next
			yield cur.data

	# 返回链表长度
	def size(self):
		cur = self.head
		count = 0

		while cur is not None:
			count += 1
			cur = cur.next

		return count

	# 插入节点
	def insert(self, index, data):
		pass

	# 删除节点
	def remove(self, idx):
		



