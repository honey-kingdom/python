
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))

print(courses[0])
print(courses[3])
print(courses[-1])
# print(courses[4])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses[0]) # A list has been inserted instead of its members

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(courses)
print(popped)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort(reverse=True)
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
# print(courses.index('Art'))
print('Art' in courses)

for item in courses:
 print(item)

for index, course in enumerate(courses, start=1):
 print(index, course)

course_str = ', '.join(courses)
print(course_str)
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)


# List - Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Tuple - Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Set - No order, No duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses) # printed in random order
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses) # No duplicates

print('Math' in cs_courses) # Set is performant for the below operations than List and Tuple

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # An empty dictionary
empty_set = set()