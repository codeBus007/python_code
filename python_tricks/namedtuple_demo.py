# coding: utf-8

from collections import namedtuple

Car = namedtuple('Car', 'color mileage weight self_defined')

def self_defined():
	print(f"my_car's color is:")

my_car = Car('red', 3812.4, 55, self_defined)
print(my_car.color)
print(my_car.mileage)
print(my_car.weight)
my_car.self_defined()

# tuple is immutable 不可变
my_car.color = 'blue'	# AttributeError: can't set attribute

