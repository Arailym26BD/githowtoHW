# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def existAndRetrievePathInfo(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    if exist_status:
        print(f"File: {os.path.basename(p)}")
        print(f"Directory: {os.path.dirname(p)}")
    else:
        print("Path is not executable")