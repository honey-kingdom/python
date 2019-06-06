import csv

with open('data/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skip the very first item
    for line in csv_reader:
        print(line[2])


with open('data/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('data\\new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)


with open('data/new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    with open('data\\new_names2.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)


with open('data/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])


with open('data/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('data\\new_names3.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


with open('data/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('data\\new_names4.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
