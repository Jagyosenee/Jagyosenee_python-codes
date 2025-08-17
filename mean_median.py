# Enter n numbers and print their mean and median.
n=int(input("Enter the elements:"))
L1=[]
for i in range(n):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The oiginal list is:",L1)

n=len(L1) 
for j in range(len(L1)): 
    for k in range (n-j-1):
        if L1[k]>L1[k+1]:
            L1[k],L1[k+1]=L1[k+1],L1[k]
print("The sorted list is:", L1)
sum_of_items=0
for items in L1:
    sum_of_items+=items
mean=sum_of_items/n
print("Mean of the the numbers is:",mean)
if n%2!=0:
    median=L1[n//2]
    print("Median of the the numbers is:",median)
else:
    median=(L1[n//2]+L1[(n//2-1)])/2
    print("Median of the the numbers is:",median)
    