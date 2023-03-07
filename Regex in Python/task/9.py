# Write a Python program to insert spaces between words starting with capital letters.

import re 
s = input() 
a = re.findall("[A-Z][^A-Z]*", s)
b = " ".join(a) 
print (b)