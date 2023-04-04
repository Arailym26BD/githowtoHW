# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re as r 
s = str(input())
n = r.findall("a.*?b$",s)
if n :
    print('yes')
else:
    print('no')