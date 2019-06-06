import csv

html_output = ''
names = []
html_output2 = ''
names2 = []

with open('data\\patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    print(csv_data)
    print(list(csv_data))


with open('data\\patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # We don't want headers or first line of bad data
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
print()


with open('data\\patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)  # able to index by 'key'

    # We don't want first line of bad data
    next(csv_data)

    for item in csv_data:
        print(item)

with open('data\\patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)  # able to index by 'key'

    # We don't want first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names2.append(f"{line['FirstName']} {line['LastName']}")

html_output2 += f'<p>There are currently {len(names2)} public contributors. Thank You!</p>'

html_output2 += '\n<ul>'

for name in names2:
    html_output2 += f'\n\t<li>{name}</li>'

html_output2 += '\n</ul>'

print(html_output2)
