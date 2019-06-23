"""
Bar Chart
"""
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))  # normalize
width = 0.25  # normalized width

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes - width, dev_y, width=width,
        color='#444444', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, width=width,
        color='#e5ae38', label='JavaScript')

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)  # match x_indexes - ages_x pair

plt.title('Median Salary (USB) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()


"""
Load Data from CSV
"""
import csv
from collections import Counter

with open('data\\data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)  # bash transposes axis

plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')

plt.tight_layout()

plt.show()


"""
Pandas for CSV
"""
import pandas as pd

data = pd.read_csv('data\\data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)  # bash transposes axis

plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')

plt.tight_layout()

plt.show()
