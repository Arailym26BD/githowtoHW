# 1
x = 5
y = "John"
print(x)
print(y)


x = 4       
x = "Sally" 
print(x)

# 2
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
print(x)
x = 'John'
print(x)


a = 4
A = "Sally"

print(a)
print(A)

# 3
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# 4
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 9
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)


# 5
x = "awesome"

def myfunc():
     print("Python is " + x)

myfunc()



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc():
      global x
      x = "fantastic"

myfunc()

print("Python is " + x)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)