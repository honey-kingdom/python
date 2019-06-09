
s0 = {}
print(type(s0))
s0 = set()
print(type(s0))


s1 = set([1, 2, 3, 4, 5])
print(s1)

s1 = {1, 2, 3, 4, 5}
print(s1)

s1 = {1, 2, 3, 4, 5, 1, 2, 3}
print(s1)

s1.add(6)
print(s1)

s1.update([6, 7, 8])
print(s1)

s2 = {7, 8, 9}
s1.update([6, 7, 8], s2)
print(s1)

s1.remove(5)
print(s1)

# s1.remove(10)  # key error. only able to remove existing item
s1.discard(10)


'''
Advanced methods
'''
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2)
print(s4)

s4 = s1.intersection(s2, s3)
print(s4)

s4 = s1.difference(s2)
print(s4)
s4 = s2.difference(s1)
print(s4)

s4 = s2.difference(s1, s3)  # that aren't in either s1 or s3
print(s4)
s4 = s3.difference(s1, s2)
print(s4)

s4 = s1.symmetric_difference(s2)  # same as s2.symmetric_difference(s1)
print(s4)


'''
Practical Example
'''
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
print(l2)


employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# who have both gym membership and is a developer
result = set(gym_members).intersection(developers)
print(result)

# who does not have neither gym membership nor is a developer
result = set(employees).difference(gym_members, developers)
print(result)



'''
Performance in membership test
'''
if 'Corey' in developers: # need to scan the whole list
    print('Found')

if 'Corey' in set(developers): # constant time, more performant
    print('Found')

# O(n) for list
# O(1) for a set
