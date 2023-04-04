# 1
a = 100
b = 35

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# 2
print(bool("Arailym"))
print(bool(7))

# 3
x = "Arailym"
y = 7

print(bool(x))
print(bool(y))

# 4
print(bool("abc"))
print(bool(123))
print(bool(["pen", "pencil", "book"]))

# 5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# 6
class myclass():
      def __len__(self):
             return 0

myobj = myclass()
print(bool(myobj))

# 7
def myFunction() :
      return True

print(myFunction())

# 8
def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# 9
x = 200
print(isinstance(x, int))