# 1
price = 50
txt = "The price is {} dollars"
print(txt.format(price))

# 2
price = 58
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# 3
quantity = 6
itemno = 456
price = 34
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# 4
quantity = 6
itemno = 456
price = 34
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# 5
age = 18
name = "Arailym"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# 6
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))