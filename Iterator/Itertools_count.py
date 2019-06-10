
import itertools

counter = itertools.count()

# beware : infinite loop
'''
for num in counter:
    print(num)
'''

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))  # zip returns an iterator
print(daily_data)


counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.count(start=5, step=-2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


data = [100, 200, 300, 400]

daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)
