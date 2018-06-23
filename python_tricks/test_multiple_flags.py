# coding: utf-8

# different ways to test multiple flags at once in python

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
	print("passed")

if 1 in (x, y, z):
	print("passed")

# These only test for truthiness
if x or y or z:
	print("passed")

if any((x, y, z)):
	print("passed")

if all((x, y, z)):
	print("passed")

"""
functionName: any: 如果存在任意一个真 元素 ，则返回 True 
type: iterable,可迭代对象
rtype: Boolean

"""


"""
functionName: all: 如果存在任意一个 非真 元素 ，则返回 False
type: iterable,可迭代对象
rtype: Boolean

"""
