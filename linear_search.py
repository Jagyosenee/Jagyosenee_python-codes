# WAP to implement linear search.
x=int(input("Enter the number of terms:"))
L1=[]
for i in range(x):
    a=int(input("Enter the elements:"))
    L1.append(a)
print("The list is:",L1)

element_to_find=int(input("Enter the element:"))
for i in range (len(L1)):
    
    if element_to_find==L1[i]:
        print("The element",element_to_find,"is in the list at the index",i) 
        break
    
else:
    print("The element",element_to_find,"is not there in the list")