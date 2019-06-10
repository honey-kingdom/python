
nums = [1, 2, 3]

for num in nums:
    print(num)

print(dir(nums))
# print(next(nums)) # TypeError: 'list' object is not an iterator (no __next__() method)

nums = [1, 2, 3]

# i_nums = nums.__iter__()
i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums)) # StopIteration (iterator has been exhausted, no more value.)


nums = [1, 2, 3]

i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):  # this class is an iterable
        return self

    def __next__(self):  # this class is an iterator
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

for num in nums:
    print(num)


nums = MyRange(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


nums = my_range(1, 10)
for num in nums:
    print(num)


def my_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)
# iterator comes in handy when writing memory efficient program
# beware : infinite loop
'''
for num in nums:
    print(num)
'''
