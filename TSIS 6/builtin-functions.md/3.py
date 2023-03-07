# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s=input()
s1=(''.join(reversed(s)))
if s==s1:
    print("Yep! Is a palindrome")
else:
    print("No")
