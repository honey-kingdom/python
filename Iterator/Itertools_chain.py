
import itertools


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']


combined = itertools.chain(letters, numbers, names) # returns a generator

for item in combined:
    print(item)
