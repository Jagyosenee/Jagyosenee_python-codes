# WAP to implement binary search.
x=int(input("Enter the number of terms:"))
L1=[]
for i in range(x):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The list is:",L1)

target=int(input("Enter the element:"))

left,right=0,len(L1)-1
result=-1

while left<=right:
    mid=(left+right)//2
    if L1[mid]==target:
        result=mid
        break
    elif L1[mid]<target:
        left=mid+1
    else:
        right=mid-1
        
if result!=-1:
    print(target,"is found at",result)
else:
    print(target,"is not found in the list")
        