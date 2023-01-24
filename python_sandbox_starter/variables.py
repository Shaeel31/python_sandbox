# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 10  # int
y = 2.5  # float
name = "John Doe"  # string
is_cool = True  # boolean

# Multiple Assignment

x, y, name, is_cool = (10, 2.15, "John Doe", True)

# Basic Maths
a = x + y

# Types & Type Conversions

print(type(x))

y = int(y)
x = float(x)
x = str(x)

print(type(x), y, name, is_cool)
