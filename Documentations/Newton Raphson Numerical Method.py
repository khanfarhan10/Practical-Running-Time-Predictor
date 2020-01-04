# Python3 code for implementation of Newton Raphson Method for solving equations 

tmax=120*10**8
#you can play around with different values of tmax
import math

 
#here we define the function whose root we want to find out
def func(x):
    g=5.049433*math.log(x)*x*x-2.024716*(x*x+1)-tmax
    return g

def derivFunc(x):
    #m=0.0001
    #l=(func(x+m)-func(x-m))/2*m
    #if you dont wish to manually find out the derivative you can uncomment the above two lines and delete the below line
    #however this may prove to be more computationally expensive
    #read Limits file for more information
    l=5.049433*(2*math.log(x)*x+x)-2.024716*2*x
    return l
# Function to find the root 
def newtonRaphson(x):
    h = func(x)/derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        x = x - h
    print("The req root is : ",x)
x0=22
#this is the initial approximation that we use 
newtonRaphson(x0) 
#code to hold the output
input("Press enter to exit!")
