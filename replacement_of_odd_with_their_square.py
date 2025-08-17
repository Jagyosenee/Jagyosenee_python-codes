#Enter 10 numbers in a list and replace the odd numbers with their square.
L1=[]
for i in range (11):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The list is:",L1)
for j in range(len(L1)):
       if L1[j]%2!=0:
        L1[j]=L1[j]**2
print("List with the square of the odds",L1)