
if True:
	print('Conditional was True')

if False:
	print('Conditional was True')

language = 'Java'
if language == 'Python':
	print('Conditional was True')
elif language == 'Java':
	print('Language is Java')
elif language == 'JavaScript':
	print('Language is JavaScript')
else:
	print('No match')

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please Log In')
else:
	print('Welcome')

a = {1, 2, 3}
b = {1, 2, 3}
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = {1, 2, 3}
b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)
print(id(a) == id(b))

condition = False
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition = None
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition = 0
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition = 10
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# Empty Sequence
condition = []
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition = ()
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

condition = ''
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# Empty Mapping
condition = {}
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')
	
condition = 'Test'
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')