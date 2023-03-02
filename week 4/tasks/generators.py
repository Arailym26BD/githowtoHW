# 1 Create a generator that generates the squares of numbers up to some number N.

import math 

def squaremaker(N):
    n = 1
    while(n <= N):
        yield n**2
        n = n + 1

N = int(input())
for squares in squaremaker(N):
    print(squares)

# 2 Write a program using generator to print the even numbers between 
# 0 and n in comma separated form where n is input from console.

import math 

def evensmaker(n):
    i = 1
    while(i <= n):
        if i % 2 == 0:
            yield i
        i += 1

n = int(input())
for i in evensmaker(n):
    print(i)

# 3 Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.

def divby3n4(max):
    n = 1
    while n <= max:
        if n % 12 == 0:
            yield n
        n += 1

n = int(input())
for i in divby3n4(n):
    print(i)


# 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    i = a
    while i <=b:
        yield i**2
        i += 1

a = int(input())
b = int(input())

for i in squares(a, b):
    print(i)

# 5 Implement a generator that returns all numbers from (n) down to 0.

import math

def numbers(max):
    i = max
    while i != 0:
        yield i
        i -= 1

max = int(input())

for i in numbers(max):
    print(i)