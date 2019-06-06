from collections import namedtuple

color = (55, 155, 255)  # tuple is immutable
print(color[0])


color = {'red': 55, 'green': 155, 'blue': 255}  # too much typing
print(color['red'])


Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)
print(color[0])
print(color.red)

color = Color(red=55, green=155, blue=255)
print(color)
