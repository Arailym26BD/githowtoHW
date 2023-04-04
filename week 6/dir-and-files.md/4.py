# Write a Python program to count the number of lines in a text file.
def countLines(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count