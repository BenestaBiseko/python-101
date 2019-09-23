'''
Write a simple script that demonstrate your understanding of functions in python 
'''
#Functions in python to print and concantnate strings

print("calculating Product of Two numbers: ")
print("Enter First Number: ")
n = float(input())
print("Enter second Number: ")
m = float(input())
def myProd(n, m):
   return float(n) * float(m)
  
myProd(n, m)
print("The Product is ", myProd(n, m))

def mySum(n, m):
  return float(n) + float(m) 
mySum(n, m)
print("The Sum is ", mySum(n, m))

def myQuo(n, m):
 return float(n) / float(m) 
myQuo(n, m)
print("The Quotient is ", myQuo(n, m))


def mySub(n, m):
 return float(n) - float(m)
mySub(n, m)
print("The Difference is ", mySub(n, m))


x = "Python is "
y = "Programming"
def mylang():

    print(x+" Awesome "+y+" Language")

mylang()

