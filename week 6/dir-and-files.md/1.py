# Write a Python program to list only directories, files and all directories, files in a specified path.
import pathlib
import os
from string import ascii_uppercase

def listDirs(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])

def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])

def listDirsAndFiles(p):
    print([x.name for x in os.scandir(path = p)])