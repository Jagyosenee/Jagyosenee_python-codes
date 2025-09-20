# WAP to sort a list in descending order using built in function.
x=int(input("Enter the number of terms:"))
L1=[]

for i in range(x):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The original list is",L1)

L1.sort()
L1.reverse()

print(L1)


# OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR OR 


x=int(input("Enter the number of terms:"))
L1=[]

for i in range(x):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The original list is",L1)
    
L1.sort(reverse=True)

print(L1)

# Built in sort always sort the list in acending order, REVERSE is a KEYWORD which is FALSE by 
# default as the list is in acending order by default. Declaring TRUE forces the list to get
# rervsed and sort the list in decending order.
