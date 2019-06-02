
import os
os.chdir('C:\\dev\\Python\\Tutorial\\data\\album')

for f in os.listdir():
	print(os.path.splitext(f))

print()

for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	print(file_name.split('-'))

print()

for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)
	f_title, f_course, f_num = f_name.split('-')
	print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

print()

for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)
	f_title, f_course, f_num = f_name.split('-')
	f_title = f_title.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:].zfill(2)
	print('{}-{}{}'.format(f_num, f_title, f_ext))
	new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
	# os.rename(f, new_name)