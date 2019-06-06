'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'


def test():
    y = 'local y'
    print(y)
    print(x)


test()
# print(y)
print(x)


def test():
    x = 'local x'
    print(x)


test()
print(x)


def test():
    global z
    z = 'global z'
    print(z)


test()
print(z)


def test(z):
    print(z)


test('local z')


m = min([5, 1, 4, 2, 3])
print(m)

import builtins
print(dir(builtins))


def my_min():
    pass


m = min([5, 1, 4, 2, 3])
print(m)


def min():
    pass

# m = min([5, 1, 4, 2, 3])


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()


def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)  # enclosing function's variable

    inner()
    print(x)


outer()


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()

x = 'global x'


def outer():
    # x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
