# coding: utf-8

import random

items = [1, 2, 3, 4, 5]

print(random.choice(items))

item_set = set(items)

# TypeError: 'set' object does not support indexing
# print(random.choice(item_set))

# random set
print(random.choice(list(item_set)))
print(random.sample(item_set, 1))
print(random.sample(item_set, 2))
