	
message = 'Hello World'
print(message)

message1 = "Bobby's World"
print(message1)

message2 = 'Bobby\'s World'
print(message2)

message3 = """Bobby's World was a good
cartoon in the 1990s"""
print(message3)

print(len(message))

print(message[0])
print(message[10])
print(message[0:5])
print(message[6:])

print(message.lower())
print(message.upper())

print(message.count('Hello'))
print(message.count('l'))

print(message.find('World'))
print(message.find('Universe'))

message.replace('World', 'Universe')
print(message)

new_message = message.replace('World', 'Universe')
print(new_message)

message = message.replace('World', 'Universe')
print(message)

greeting = 'Hello'
name = 'Michael'
message = greeting + name
print(message)

message = greeting + ', ' + name
print(message)

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name}. Welcome!'
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
print(help(str))
print(help(str.lower))