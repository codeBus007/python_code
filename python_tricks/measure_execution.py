# coding: utf-8

import timeit


print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

print(timeit.timeit('"_".join([str(n) for n in range(100)])', number=10000))

print(timeit.timeit('"_".join(map(str, range(100)))', number=10000))