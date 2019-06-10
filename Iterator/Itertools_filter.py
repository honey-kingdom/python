
import itertools


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

print('Compress')
result = itertools.compress(letters, selectors)

for item in result:
    print(item)

 # filter


def lt_2(n):
    if n < 2:
        return True
    return False


print('Filter')
result = filter(lt_2, numbers)

for item in result:
    print(item)


print('FilterFalse')
result = itertools.filterfalse(lt_2, numbers)

for item in result:
    print(item)


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']


print('DropWhile')
result = itertools.dropwhile(lt_2, numbers)

for item in result:
    print(item)


print('TakeWhile')
result = itertools.takewhile(lt_2, numbers)

for item in result:
    print(item)
