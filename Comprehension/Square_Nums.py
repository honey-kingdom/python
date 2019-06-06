def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)





def square_numbers(nums):
    result = []
    for i in nums:
        yield(i * i)

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums)) # entire generator is exhausted



my_nums = square_numbers([1, 2, 3, 4, 5])

for num in my_nums:
    print(num)

my_nums = [x * x for x in [1, 2, 3, 4, 5]]

print(my_nums)
for num in my_nums:
    print(num)



my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(my_nums)
print(list(my_nums)) # but performance degradation when handling a big data structure
