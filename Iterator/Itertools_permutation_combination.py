
import itertools


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)
for item in result:
    print(item)


result = itertools.permutations(letters, 2)
for item in result:
    print(item)


result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)


result = itertools.combinations_with_replacement(numbers, 4)
for item in result:
    print(item)
