# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generateFiles():
    for ch in ascii_uppercase:
        file = open(f"./files/{ch}.txt", 'x')
        file.close()

    print("All files have been successfully generated")
