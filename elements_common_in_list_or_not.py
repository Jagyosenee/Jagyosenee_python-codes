# Given two lists, write a program that checks if they have any elements in common using 
# in or not in.
x=int(input("Enter the no of terms:"))
L1=[]
for i in range (1,x+1):
    a=(input("Enter the elements:"))
    L1.append(a)
print("The first list is:",L1)
y=int(input("Enter the no of terms:"))
L2=[]
for j in range (1,y+1):
    b=(input("Enter the elements:"))
    L2.append(b)
print("The second list is:",L2)
element_to_check=input("Enter the element:")
if element_to_check in L1 and L2:
    print("The element",element_to_check,"is common in both the lists")
else:
    print("The element",element_to_check,"is not common in both the lists")