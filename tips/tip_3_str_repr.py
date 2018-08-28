# coding: utf-8
"""
str()：便于可读性
repr(): 便于精确性
"""


class A(object):
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'<A(name: {self.name})>'

a1 = repr(A("zhang"))
a2 = A("lin")


print(type(a1))
print(a2)