# Write a python program to convert snake case string to camel case string.
import re 
s = input()
def convert(s):
    return ''.join(x.capitalize() for x in s.split("_"))
print(convert(s))