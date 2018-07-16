# coding: utf-8

a, b = 10, 20

print(a, b)

a, b = b, a
print(a, b)


class A(object):
	
	_DEMO = 'ok'
	def __init__(self):
		self._DOMAIN = "www.baidu.com"
		self._LOGIN = self._DOMAIN + "/login.html"

	def printLogin(self):
		print(self._LOGIN)


class B(A):
	_URL = 'www.google.com'
	def __init__(self):
		super(B, self).__init__()
		self._DOMAIN = "www.google.com"
		self._LOGIN = self._DOMAIN + "/login.html"

a = A()
b = B()

print(a._LOGIN)
print(b._LOGIN)

b.printLogin()