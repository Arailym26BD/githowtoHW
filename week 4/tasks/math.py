# 1 Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904

import math

degree = float(input())
radian = math.radians(degree)
print(radian)


# 2 Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

import math

a = float(input())
b = float(input())
h = float(input())

print (0.5 * (a + b) * h)


# 3 Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math

n = float(input())
l = float(input())

x = (math.radians(180))/n
ctg = 1/(math.tan(x))

print( 0.25 * n * (l * l) * ctg)


# 4 Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

import math

base = float(input())
height = float(input())

print (base * height)