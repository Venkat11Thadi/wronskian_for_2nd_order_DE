import cmath
from sympy import *

x = symbols('x')

print("Enter values of a,b,c in 2nd order DE( ay'' + by' + cy = 0 )-")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

det = b**2-4*a*c

r1= (-b+cmath.sqrt(float(det)))/2*a
r2= (-b-cmath.sqrt(float(det)))/2*a

a1=complex(r1)
a2=complex(r2)

if(a1.real==a2.real and (a1.imag == 0 and a2.imag == 0)):
    fun1=exp(a1.real*x)
    fun2=x*exp(a1.real*x)

elif(a1.imag == 0 and a2.imag == 0):
    fun1 = exp(a1.real*x)
    fun2 = exp(a2.real*x)

else:
    fun1 = exp(a1.real*x)*(cos(a1.imag*x))
    fun2 = exp(a2.real*x)*(sin(a2.imag*x))

#print("Expression : A{}+B{} ".format(fun1),format(fun2))

# Use sympy.Derivative() method
expr_diff1 = diff(fun1,x)
expr_diff2 = diff(fun2,x)

#print("Derivative of expression with respect to x : {}".format(expr_diff1))
print("Value of the derivative-1 : {} ".format(expr_diff1))
print("Value of the derivative-2 : {} ".format(expr_diff2))

print("Wronskian is: {}".format(fun1*(expr_diff2) - fun2*(expr_diff1)))

if(fun1*(expr_diff2) - fun2*(expr_diff1)==0):
    print("functions are linearly dependent...")
else:
    print("functions are linearly independent...")