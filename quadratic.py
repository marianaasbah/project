import math 
from turtle import*
def quadratic(x):
    return x**2 -17*x +12

setworldcoordinates(-100, -50, 100, 1000)
speed (20)
bgcolor('black')

for i in range (-20,38):
    goto(i,quadratic(i))
    color("#f73487")

done()

