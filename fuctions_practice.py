#Functions
def add(): #function defination
    num_1=19 #function body
    num_2=20
    print(num_1+num_2)
add()

def looping():
    for i in range(20):
        print(i)
looping()

#Parameters and arguments
def multiply(a,b):
    print(a*b)
multiply(5,6)# 5 and 6 are arguments
multiply(667,10)
multiply(60,60)
multiply(7,9)
multiply(6,7)
multiply(33,10)

#Using input
def multiply(x,y):
    print(x*y)
x=int(input("enter number"))
y=int(input("enter number"))
multiply(x,y)
multiply(x,y)

#Default Prameters
def details(user=None,dept=None,id=None):
    print(user,dept,id)
details("anusha","physics",111)
details("akshitha", "maths",)
details("akshara",)
details()

#example
def discount(price,discount=2):
    discount_amount=(price*discount)/100
    final_price=price-discount_amount
    print(final_price)
discount(5000,10)
discount(2000)
discount(100000,30)
discount(200000)

#arbitary arguments  functions can accept a variable number of arguments by using *args
def sample(*a):#multiple arguments to one variable
    print(a)
sample("anu","akki",25, 13)
print(type(sample))

#keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter
def sample(**a):
    print(a)
sample(a=10,b=20,c=30)

#*use=tuple, **= dictionary format

#variables 2 types 
#local variables  inside the function
#global variables outside th function, inside function 

#return Statement
def add(n_1,n_2):
    return n_1+n_2 #to exit the function
print(add(45,78))

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def expo(a,b):
    print(a**b)
sub(10,5)# by using function calling
sub(60,70)

#collection of functions called as module, every python file is a module
#3 types of modules
#1 user defind module ,2 builtin module,3 3rd party module

import fuctions_practice
fuctions_practice.add(20,20)
fuctions_practice.expo(5,5)

from fuctions_practice import *# * means all
add(78,10)
mul(43,90)

#math Module
import math
# modulename.function name
print(math.sqrt(36))

from math import*
print(pow(8,2))
print(cos(1))

# from random import
import random
print(random.randint (1,6))#random integer between 
print(random.choice(["apple","pomogranate","orange"]))#randomly choose from a list

#Date and time
from datetime import datetime
now=datetime.now()
print(now)


