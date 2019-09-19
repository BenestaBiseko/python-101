'''
Write a simple script that demonstrate your understanding of Operators,operands and operator precedence
'''
# A script for demonstrate operators, operands and operator precedence

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


def myMod(n, m):
 return float(n) % float(m)
myMod(n, m)
print( n," Module of ", m, "Is ", myMod(n, m))




x = "Python is "
y = "Programming"
def mylang():

    print(x+" Awesome "+y+" Language")

mylang()

