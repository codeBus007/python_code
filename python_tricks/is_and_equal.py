# coding: utf-8

a = [1, 2, 3]
b = a 

print(a is b)

print(a == b)


c = list(a)
print(a == c)
print(a is c)

# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal