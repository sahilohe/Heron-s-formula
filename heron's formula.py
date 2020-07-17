#Heron's formula

#import square root function freom math library
from math import sqrt

#the users enter the sides of the triangle
a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))

#the semi-perimeter with variable 's'
s = (a + b + c) / 2

#let's find the area
area = sqrt(s * (s-a) * (s-b) * (s-c)) #heron's formula
print(round(area,3)) #prints the result or answer to the decimal values of 3
