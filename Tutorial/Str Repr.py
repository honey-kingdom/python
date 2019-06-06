a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))

print()

print(str(b))
print(repr(b))

print()


# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable


import datetime

# can be replaced with tzinfo=pytz.UTC with pytz package
a = datetime.datetime.utcnow().replace(tzinfo=None)
b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print()

# repr is really for developers
print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

print()
