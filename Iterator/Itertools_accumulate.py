
import itertools


numbers = [0, 1, 2, 3, 2, 1, 0]

result = itertools.accumulate(numbers)

for item in result:
    print(item)


import operator

numbers = [1, 2, 3, 2, 1, 0]

result = itertools.accumulate(numbers, operator.mul)

for item in result:
    print(item)
