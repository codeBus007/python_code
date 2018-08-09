# coding: utf-8

from random import randint
from retrying import retry


# print(1 / 0)
def retry_if_ZeroDivisionError(exception):
	return isinstance(exception, ZeroDivisionError)

def retry_if_result_bigger_than_5(result):
	return result > 5

@retry(stop_max_attempt_number=3, wait_random_min=1000, wait_random_max=2000,retry_on_exception=retry_if_ZeroDivisionError, retry_on_result=retry_if_result_bigger_than_5)
def dive():
	a = randint(1, 100)
	b = 5
	return a / b

if __name__ == '__main__':
	dive()