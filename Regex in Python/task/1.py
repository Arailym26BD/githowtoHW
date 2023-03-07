# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re 
s = str(input())
n = re.search('^a(b*)$' , s) 
if n :
    print ("Yes") 
else :
    print ("No")