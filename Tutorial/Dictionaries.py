
student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}

print(student['name'])
print(student['courses'])

student = {1: 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}
print(student[1])

student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}
# print(student['phone']) # Key error when key does not exist
print(student.get('name'))
print(student.get('phone'))

# Default value when key does not exist
print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

student['name'] = 'Jane'
print(student)

student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

del student['age']
print(student)

student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}
age = student.pop('age')
print(student)
print(age)

student = {'name': 'John', 'age': 25, 'courses': {'Math', 'CompSci'}}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
