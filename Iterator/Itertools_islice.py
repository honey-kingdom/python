
import itertools


result = itertools.islice(range(10), 5)

for item in result:
    print(item)


result = itertools.islice(range(10), 1, 5)

for item in result:
    print(item)


result = itertools.islice(range(10), 1, 5, 2)

for item in result:
    print(item)


with open('data\\test.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')
