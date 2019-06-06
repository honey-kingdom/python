"""
Context Manager using a class
"""


class Open_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # set-up
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):  # tear-down
        self.file.close()


with Open_file('data\\sample.txt', 'w') as f:  # with statement runs __enter__ method
    f.write('Testing')

print(f.closed)


"""
Context Manager using a function
"""
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    f = open(file, mode)  # equivalent to __enter__
    yield f
    f.close()  # equivalent to __exit__


with open_file('data\\sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)


# error handling version
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('data\\sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)


# practical example
import os

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield  # no output
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
