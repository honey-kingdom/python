
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

print('\tTab')
print(r'\tTab')  # raw string


pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])


# pattern = re.compile(r'.')
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\S')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)

for match in matches:
    print(match)


pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)

for match in matches:
    print(match)


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


with open('data\\data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)


pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # character set
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


with open('data\\data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)


pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'[a-z]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'[^a-zA-Z]')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# quantifier
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# findall() method with groups
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)

for match in matches:
    print(match)


# without any group
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.findall(text_to_search)

for match in matches:
    print(match)


# match() method only searches a string at the beginning
pattern = re.compile(r'Start')
matches = pattern.match(sentence)

print(matches)



pattern = re.compile(r'sentence')
matches = pattern.match(sentence)

print(matches)



# search() method searches the first string that matches within the entire string
pattern = re.compile(r'sentence')
matches = pattern.search(sentence)

print(matches)



# flags
pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.search(sentence)

print(matches)



pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)

print(matches)
