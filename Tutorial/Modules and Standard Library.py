
import my_module
courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')
print(index)

import my_module as mm
courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index # test variable has not been imported yet
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)

from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)

from my_module import find_index as fi, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = fi(courses, 'Math') # Not really readable
print(index)

from my_module import *
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)

from my_module import find_index, test ### better to do in this way ###
import sys
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(sys.path)

import sys
sys.path.append('C:\\dev\\Python\\Tutorial')
from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(sys.path)

import random # standard library : random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

import math # standard library : random
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime # standard library : datetime
import calendar # standard library : calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))
print(calendar.isleap(2020))

import os # standard library : os (accesses to underlying operation system)
# create, scan, delete files, etc.
print(os.getcwd()) # current working directory
print(os.__file__)

import antigravity