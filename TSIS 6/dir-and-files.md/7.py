# Write a Python program to copy the contents of a file to another file
f1=open("icopiedfromhere.txt", "r")
f2=open("tohere.txt", "w")
for line in f1:
    f2.write(line)