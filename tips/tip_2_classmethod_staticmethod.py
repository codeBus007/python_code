# coding: utf-8

# classmethod 与 staticmethod 的区别

"""
静态方法和类方法都可以通过 类名.方法名 或 实例.方法名 的形式来访问
其中静态方法没有常规方法的特殊行为 如绑定/非绑定/隐式参数等规则
而类方法的调用使用类本身作为其隐含参数,但调用本身并不需要显示提供该参数
"""

class A(object):
	def instance_method(self, x):
		print("calling instance_method instance_method(%s, %s)" % (self, x))

	@classmethod
	def class_method(cls, x):
		print("calling class_method class_method(%s, %s)" % (cls, x))

	@staticmethod
	def static_method(x):
		print("calling static_method static_method(%s)" % x)

###############################

# class Fruit(object):
# 	total = 0

# 	@classmethod
# 	def print_total(cls):
# 		print(cls.total)

# 	@ classmethod
# 	def set_total(cls, value):
# 		cls.total = value

# class Apple(Fruit):
# 	pass

# class Orange(Fruit):
# 	pass
###############################

# class Fruit(object):
# 	def __init__(self, area="", category="", batch=""):
# 		self.area = area
# 		self.category = category
# 		self.batch = batch

# 	@staticmethod
# 	def Init_Product(product_info):
# 		area, category, batch = map(int, product_info.split('-'))
# 		fruit = Fruit(area, category, batch)
# 		return fruit

# class Apple(Fruit):
# 	pass

# class Orange(Fruit):
# 	pass
###############################
# class Fruit(object):
# 	def __init__(self, area="", category="", batch=""):
# 		self.area = area
# 		self.category = category
# 		self.batch = batch

# 	@classmethod
# 	def Init_Product(cls, product_info):
# 		area, category, batch = map(int, product_info.split('-'))
# 		fruit = cls(area, category, batch)
# 		return fruit

# class Apple(Fruit):
# 	pass

# class Orange(Fruit):
# 	pass

def is_input_valid(product_info):
	area, category, batch = map(int, product_info.split('-'))

	try:
		assert 0 <= area <= 10
		assert 0 <= category <= 15
		assert 0 <= batch <= 99
	except AssertionError:
		return False
	return True

if __name__ == "__main__":


	# a = A()
	# a.instance_method("test")
	# a.class_method("test")
	# a.static_method("test")

	###############################

	# app1 = Apple()
	# app1.set_total(200)
	# app2 = Apple()

	# org1 = Orange()
	# org1.set_total(300)
	# org2 = Orange()

	# app1.print_total()
	# org1.print_total()

	###############################
	# app1 = Apple(2, 5, 10)
	# org1 = Orange.Init_Product("2-3-9")

	# print("app1 is instance of Apple:" + str(isinstance(app1, Apple)))
	# print("org1 is instance of Orange:" + str(isinstance(org1, Orange)))

	################################
	# app1 = Apple(2, 5, 10)
	# org1 = Orange.Init_Product("2-3-9")

	# print("app1 is instance of Apple:" + str(isinstance(app1, Apple)))
	# print("org1 is instance of Orange:" + str(isinstance(org1, Orange)))

	#############################
	print(is_input_valid("99-100-109"))
	print(is_input_valid("1-2-99"))

