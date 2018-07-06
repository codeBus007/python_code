# coding: utf-8

age = 15
print("kid" if age < 13 else "teenager" if age < 18 else "adult")


# 如果 []内为True. 默认 选 tuple 右边
print((("teenager", "kid")[age < 13], "adult")[age > 18])

# 加 key 操作
print({True: {True: 'teenager', False: 'kid'}[age < 13], False: "adult"}[age > 18])


def hello():
	print("hello")

def world():
	print("world")


(hello, world)[age < 13]()