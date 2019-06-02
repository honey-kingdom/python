# File Objects
f = open('data\\test.txt', 'r')
# f = open('data\\test.txt', 'w')
# f = open('data\\test.txt', 'r+')
print(f.name)
print(f.mode)
f.close()

with open('data\\test.txt', 'r') as f: # context manager
	pass
print(f.closed)
# print(f.read())

with open('data\\test.txt', 'r') as f:
	f_contents = f.read()
	print(f_contents)

with open('data\\test.txt', 'r') as f:
	f_contents = f.readlines()
	print(f_contents)

with open('data\\test.txt', 'r') as f:
	f_contents = f.readline()
	print(f_contents)
	f_contents = f.readline()
	print(f_contents, end='')

with open('data\\test.txt', 'r') as f:
	for line in f:
		print(line, end='')

with open('data\\test.txt', 'r') as f:
	f_contents = f.read(100)
	print(f_contents, end='')
	f_contents = f.read(100)
	print(f_contents, end='')
	f_contents = f.read(100)
	print(f_contents, end='')

with open('data\\test.txt', 'r') as f:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents, end='*')
		f_contents = f.read(size_to_read)

with open('data\\test.txt', 'r') as f:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end='')
	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents)

with open('data\\test2.txt', 'w') as f:
	f.write('Test')
	f.seek(0) # seek is tricky when writing on a file
	f.write('R')

with open('data\\test.txt', 'r') as rf:
	with open('data\\test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

with open('data\\image.bmp', 'rb') as rf:
	with open('data\\image_copy.png', 'wb') as wf:
		for line in rf:
			wf.write(line)

with open('data\\image.bmp', 'rb') as rf:
	with open('data\\image_copy.bmp', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)