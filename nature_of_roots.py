#Enter the coefficient of a quadratic equation and print the nature of its root.
a=int(input("enter the coefficient of x^2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant:"))
D=b**2-4*a*c
if D>0:
    print("The roots are real and distict")
elif D==0:
    print("The roots are equal")
else:
    print("The roots are complex")
    