# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re 
s = str(input())
n = re.search('^ab{2,3}',s)
if n :
    print ("Yes")
else :
    print("No")