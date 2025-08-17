#Enter the coefficient of a quadratic equation and print its root.
import math
a=int(input("enter the coefficient of x^2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant:"))
D=b**2-4*a*c
root1=(-b+math.sqrt(D))/(2*a)
root2=(-b-math.sqrt(D))/(2*a)
print("The roots of the quadratic equation are",root1,root2)