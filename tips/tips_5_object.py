# coding: utf-8
"""
区分 可变对象 与 不可变对象
	不可变对象	数字/字符串/元组
	可变对象		字典/列表/字节数组

使用 id() 函数检查对象是否一致

"""
# teststr = 'I am a pytlon string'
# 错误的修改字符串

# teststr[10] = 'h'
# print(teststr)

# class Student(object):
# 	def __init__(self, name, course=None):
# 		self.name = name
# 		if course is None:
# 			self.course = []

# 	def addCourse(self, course):
# 		self.course.append(course)

# 	def printCourse(self):
# 		for item in self.course:
# 			print(item)

# stuentA = Student("John")
# stuentA.addCourse('Math')
# stuentA.addCourse('Chinese')
# print("stuentA's course:")
# stuentA.printCourse()
# print("=================")

# stuentB = Student('Mary')
# stuentB.addCourse('English')
# print("stuentB's course:")
# stuentB.printCourse()
# print(id(stuentA.course))
# print(id(stuentB.course))


# list1 = ['a', 'b', 'c']
# list2 = list1
# print(id(list1))
# print(id(list2))
# list1.append('d')
# print(list2)


# list3 = list1[:] # 切片 相当于浅拷贝
# list3.remove('a')
# print(list1)
# print(id(list3))	# 此时 list3 与 list1 / list2 已经不同了


def my_list(list1=[]):
	for i in 'abcdefg':
		list1.append(i)
	print(list1)

my_list()
my_list()




# 不可变对象
# a = 1
# print(id(a))

# a += 2	

# print(id(a))	# 生成新的 对象 ，之前的被回收销毁


# str1 = "hello world"

# str2 = str1
# print(id(str1))
# print(id(str2))

# str1 = str1[:-5]
# print(str1)
# print(id(str1))





