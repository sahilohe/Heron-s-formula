#Heron's formula

#import square root function freom math library
from math import sqrt

a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))

#the semi-perimeter
s = (a + b + c) / 2

#let's find the area
area = sqrt(s * (s-a) * (s-b) * (s-c))
print(round(area,3))
