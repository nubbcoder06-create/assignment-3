import math
from math import radians

global n

n = float(input("enter a number:"))

def squareroot(n):
    return math.sqrt(n)
ans = squareroot(n)
print("Square root:",ans)

def log(n):
    return math.log(n)
ans2 = log(n)
print("Log root:",ans2)

def sin(n):
    rad = math.radians(n)
    return math.sin(rad)
ans3 = math.sin(n)
print("Sine root:",ans3)


