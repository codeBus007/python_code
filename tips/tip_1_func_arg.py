# coding: utf-8

# tip_1 python 函数传参既不是传值也不是传引用


# 下面的列子说明 不是传引用
def inc(n):
	print(id(n))
	n = n + 1
	print(id(n))

n = 3

print(id(n))	# 4305324480

inc(n)	# 4305324480	4305324512

print(n)	# 3

# 下面例子说明 不是传值
def change_list(orginal_list):
	print('orginal_list is :', orginal_list)

	new_list = orginal_list
	new_list.append('i am new')
	print('new_list is: ', new_list)
	return new_list

orginal_list = ['a', 'b', 'c']
new_list = change_list(orginal_list)

print(new_list)
print(orginal_list)

# 下面例子说明 不是 可变对象传引用 不可变对象传值
def change_me(org_list):
	print(id(org_list))
	new_list = org_list
	print(id(new_list))

	if len(new_list) > 5:
		new_list = ["a", "b", "c"]

	for i, e in enumerate(new_list):
		if isinstance(e, list):
			new_list[i] = "***"
	print(new_list)
	print(id(new_list))

test1 = [1, ['a', 1, 3], [2, 1], 6]
change_me(test1)
print(test1)
test2 = [1, 2, 3, 4, 5, 6, [1]]
change_me(test2)
print(test2)

# 正解
"""
传对象的或者说传对象的引用
	对于可变对象的修改 在函数内外部都可见 调用者和被调用者共享这个对象
	对于不可变对象的修改 由于并不能真正地被修改 因此修改往往是通过生成一个新对象 然后赋值来实现的
"""
a = 5
print(id(a))

b = a
print(id(b))

b = 7

print(id(b))
print(id(a))




