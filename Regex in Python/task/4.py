# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re as r
s = str(input())
n = r.findall("[A-Z]+[a-z]$",s)
if n :
    print ("YES")
else :
    print ('NO')