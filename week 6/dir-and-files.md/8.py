# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os
p=(r"https://github.com/Arailym26BD/pp2-2023.git.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")