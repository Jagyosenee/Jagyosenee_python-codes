#Write a program that takes a list of numbers and creates a new list containing only the 
# even numbers.
x=int(input("Enter the no of terms:"))
L1=[]
for i in range (1,x+1):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The original list is:",L1)
even_list=[]
for j in L1:
    if j%2==0:
     even_list.append(j)
print("The list containing even numbers are",even_list)