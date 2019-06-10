
import itertools


counter = itertools.repeat(2)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# repeat is normally used for passing a constant value to map or zip functions
squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))


squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])

print(list(squares))
