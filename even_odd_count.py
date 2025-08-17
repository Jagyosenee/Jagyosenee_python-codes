# Enter 10 numbers in a list and print the count of odd and even numbers separately.
L1=[]
for i in range (11):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The list is:",L1)
even = 0
odd = 0
for j in L1:
    if j%2==0:
        even+=1
    else:
        odd+=1
print("The number of odd numbers are",odd)
print("The number of even numbers are",even)
   
        