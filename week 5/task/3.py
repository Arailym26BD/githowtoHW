# Write a Python program to find sequences of lowercase letters joined with a underscore
import re 
s = str(input())
x = re.findall("[a-z]",s)
if x : 
    print("Yes")
else :
    print("No")