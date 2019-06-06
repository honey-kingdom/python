
import os

print(dir(os))
print(os.getcwd())
os.chdir('C:\\dev\\Python\\Tutorial')

print(os.getcwd())
print(os.listdir())

os.mkdir('OS-Demo-2')
print(os.listdir())
os.rmdir('OS-Demo-2')

os.makedirs('OS-Demo-3/Sub-Dir-1')
print(os.listdir())
os.removedirs('OS-Demo-3/Sub-Dir-1')

os.rename('data\\demo.txt', 'data\\demo.txt')
print(os.stat('data\\demo.txt').st_size)
print(os.stat('data\\demo.txt').st_mtime)

from datetime import datetime

mod_time = os.stat('data\\demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


	
for dirpath, dirnames, filenames in os.walk('C:\\dev\\Python'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))