# coding: utf-8
def dispatch_if(operator, x, y):
	if operator == 'add':
		return x + y
	if operator == 'sub':
		return x - y
	if operator == 'mul':
		return x * y
	if operator == 'div':
		return x / y
	return None


def dispatch_dict(operator, x, y):
	return {
		'add': lambda: x + y,
		'sub': lambda: x - y,
		'mul': lambda: x * y,
		'div': lambda: x / y
	}.get(operator, lambda:None)()

print(dispatch_if('add', 2, 8))
print(dispatch_dict('mul', 2, 8))
print(dispatch_if('unknown', 2, 8))
print(dispatch_dict('unknown', 2, 8))

