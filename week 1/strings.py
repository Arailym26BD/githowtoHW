# 1
print("Arailym")
print('Arailym')

# 2
a = "Arailym"
print(a)

# 3
a = """Arailym"""
print(a)

# 4
a = '''Arailym'''
print(a)

# 5
a = "Arailym"
print(a[1])

# 6
for x in "Kbtu":
  print(x)

# 7
a = "Arailym"
print(len(a))

# 8
txt = "Kbtu top"
print("Kbtu" in txt)

# 9
txt = "Kbtu is the best university in Kazakhstan"
if "Kazakhstan" in txt:
  print("Yes, 'Kazakhstan' is present.")

#  10
xt = "Kbtu is the best university in Kazakhstan"
print("worse" not in txt)

# 11
txt = "Kbtu is the best university in Kazakhstan"
if "worse" not in txt:
  print("No, 'worse' is NOT present.")

# 12
b = "Arailym"
print(b[:5])

# 13
b = "Arailym"
print(b[2:])

# 14
b = "Arailym"
print(b[-5:-2])

# 15
a = "Arailym"
print(a.upper())

# 16
a = "Arailym"
print(a.lower())

# 17
a = "Arailym"
print(a.strip())

# 18
a = "Arailym"
print(a.replace("A", "m"))

# 19
a = "Arailym"
print(a.split(","))

# 20
a = "Kbtu"
b = "top"
c = a + b
print(c)

# 21
a = "Kbtu"
b = "top"
c = a + " " + b
print(c)

# 22
age = 18
txt = "My name is Arailym, I am {}"
print(txt.format(age))

# 23
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# 24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 25
txt = "We are the so-called \"Arailym\" from the north."
print(txt)