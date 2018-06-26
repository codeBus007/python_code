# coding: utf-8

# How to merge dictionaries in python 3.5+

x = {"a": 1, "b":12}
y = {"b": 2, "c": 3}

z = {**x, **y}
print(z)


# python 2.x

z = dict(x, **y)
print(z)

err_msg = None
if False:
	err_msg = "ok"

err_msg = err_msg if err_msg is not None else "not ok"
print(err_msg)