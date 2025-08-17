# Enter the coefficient of a quadratic equation and print the nature of its root.
num=int(input("Enter the number:"))
rev=0
copy=num
while num>0:
    rev=rev*10+num%10
    num//=10
if rev==copy:
    print(copy,"is a palindrome number")
else:
    print(copy,"is not a palindrome number")