# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re 
s = input()
n = re.sub("[\s.,] , :" , s)
print(n)