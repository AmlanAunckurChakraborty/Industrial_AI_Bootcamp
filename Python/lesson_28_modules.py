#Modules
print("\n===MODULES===\n")

#Python defined Modules

#import whole module 
print("\n===IMPORT WHOLE MODULES===\n")
import math
print(math.sqrt(25))
print(math.pi)

#import specific funtion from modules
print("\n===IMPORT SPECIFIC FUNTIONS FROM MODULES===\n")
from math import sqrt
print(sqrt(36))

#Assigning alias
print("\n===IMPORT WHOLE MODULES WITH ALIAS===\n")
import math as m
print(m.sqrt(49))

#random will come after some time
print("\n===IMPORT WHOLE MODULES WITH ALIAS RANDOM===\n")
import random as rnd
for i in range(10):
 print(rnd.randint(1,100))

 #MODULES MATH 
print ("\n ====math===\n")
import math as m
print(math.pi) # simply constant π we used in math circumferance/redious
print("pi",m.pi) #both will work the original module name and the alias like amlan as 1st person and he as 3rd both define one man
print("e",m.e) #same euler number e
print("squre root",m.sqrt(100)) #same suare root in algebra
print("power",m.pow(2,3)) #same as ** 2**3
print("factorial",m.factorial(0)) #handle 0! also as its a comple math funtion
#round up
print("ceil",m.ceil(43.001)) # Always rounds UP to the next integer
#round down
print("floor",m.floor(42.9999)) #Always go to the largest integer less than or equal to the number.
print("floor",m.floor(-42.499)) #Floor always moves down on the number line.
# dont round just delete decimal
print("trunc",m.trunc(42.999)) # #trunc means delete after decimal and give the just before int
print("trunc",m.trunc(-42.999)) # #trunc means delete after decimal and give the just before int
#proper algebric or banking round to clear confution
print("rount",round(42.99)) #not a math function but actually rounds like algebra 42.49=42 and 42.51=43
print("rount",round(42.5)) #Python uses Banker's Rounding,When the fractional part is exactly .5, Python rounds to the nearest even integer.
print("rount",round(43.5)) 
print("fabs",m.fabs(-12.3)) # gives absulate value
print("abs",abs(-1.6)) # math module has fabs and python has abs
print("log",m.log(100)) #natural log e base
print("log10",m.log10(100)) #10base log

print("sin(radian)",m.sin(.524)) #takes redian by default using decimal value need to be accurate this value wont work up to 3decimal
print("sin(radian)",m.sin((m.pi)/6)) #takes redian by default, so writing with pi is a best
print("sin(degree)",m.sin(m.radians(30))) #takes redian by default to convert to degree by radius
print("inverse sin(radian)",m.asin(.5)) #sin inverse in radian
print("inverse sin(degree)", m.degrees(m.asin(.5))) #sin inverse in degree
print("sinh(x) hyperbolic",m.sinh(.5)) #hyperbolic sin

print("cos(x)",m.cos(m.radians(45)))  #takes redian by default, so writing with pi is a best
print("inverse cos(radian)",m.acos(.5)) #cos inverse in radian
print("inverse cos(degree)", m.degrees(m.acos(.5))) #cos inverse in degree
print("cos(x) hyperbolic",m.cosh(.707)) #hyperbolic cos

print("tan(x)",m.tan(m.radians(30)))  #takes redian by default, so writing with pi is a best
print("inverse tan(radian)",m.atan(1)) #tan inverse in radian
print("inverse tan(degree)",m.degrees(m.atan(1)))
print("inverse tan(degree)",m.degrees(m.atan(.577))) #tan inverse in degree but dont work pi now as not angle but ratio so works better with decimal value
print("inverse tan(degree) with pi",m.degrees(m.atan((m.pi)/6))) #wont work decimal better
print("tanh(x) hyperbolic",m.tanh(60))  #hyperbolic tan



        
