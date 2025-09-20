# WAP to sort number in even indices in ascending order and number in odd indices in descending order.
def decending_sort(n):
    x=len(n)
    for j in range(x): 
        for k in range (x-j-1):
            if n[k]<n[k+1]:
                n[k],n[k+1]=n[k+1],n[k]
    return n

def acending_sort(n):
    x=len(n)
    for j in range(x): 
        for k in range (x-j-1):
            if n[k]>n[k+1]:
                n[k],n[k+1]=n[k+1],n[k]
    return n

x=int(input("Enter the number of terms:"))
L1=[]
L_even=[]
L_odd=[]

for i in range(x):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The unsorted list is:",L1)

for i in range(len(L1)):
    if i%2==0:
        L_even.append(L1[i])
    else:
        L_odd.append(L1[i])
        
print("Unsorted list with the elements of even indices:",L_even)
print("Unsorted list with the elements of odd indices:",L_odd)
print("Sorted list with the elements of even indices:",acending_sort(L_even))
print("Sorted list with the elements of odd indices:",decending_sort(L_odd))
