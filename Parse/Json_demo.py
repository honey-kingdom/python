import json

people_string = '''
{
    "people": [
      {
        "name": "John Smith",
        "phone": "615-555-7164",
        "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
        "has_license": false
      },
      {
        "name": "Jane Doe",
        "phone": "560-555-5153",
        "emails": null,
        "has_license": true
      }
    ]
}
'''

data = json.loads(people_string)

print(data)
print(type(data))
print(type(data['people']))

for person in data['people']:
    print(person)

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_string = json.dumps(data)
print(new_string)

new_string = json.dumps(data, indent=2)
print(new_string)

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


with open('data\\states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('data\\new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
