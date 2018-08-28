# coding:utf-8

"""
tips:
	*args 元组变长	
	**kwargs 字典变长
	变长参数用的过度(不考虑可读性)，不利于团队工作

	一般应用的几种情况
	1、装饰器
	2、继承或或多态时 
"""

def my_dec(func):
	def new(*args, **kwargs):
		print("in new")
		return func(*args, **kwargs)

	return new

@my_dec
def myfunc(a, b):
	print(a, b)

myfunc(1,2)


class A(object):
	def __init__(self, a, b):
		print(a,b)

class B(A):
	def __init__(self, c, *args, **kwargs):
		super(B, self).__init__(*args, **kwargs)
		print(c)

b = B(1,2,3)
