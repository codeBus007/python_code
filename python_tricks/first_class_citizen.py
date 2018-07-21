# coding: utf-8
def myFunc(a, b):
	return a + b

def myFunc_2(a, b):
	return a - b

def myFunc_3(a, b):
	return a * b

def myFunc_4(a, b):
	return a / b

funcs = [myFunc, myFunc_2, myFunc_3, myFunc_4]


for func in funcs:
	print(func(2, 3)) 