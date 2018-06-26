# coding: utf-8

xs = {"a": 4, "b": 3, "c": 2, "d": 1}

a = sorted(xs.items(), key=lambda x: x[1])

for ao in a:
	print(ao[0], ao[1])
print(xs)


import operator
print(dir(operator))
print(sorted(xs.items(), key=operator.itemgetter(1)))

print(xs)