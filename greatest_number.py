# Enter n numbers and print the greatest.
x=int(input("Enter the number of terms:"))
original_list=[] 
for i in range(x):
    a=int(input("Enter the elements:"))
    original_list.append(a)
print("The oiginal list is:",original_list)
n=len(original_list)  
for j in range(len(original_list)): 
    for k in range (n-j-1):
        if original_list[k]>original_list[k+1]:
            original_list[k],original_list[k+1]=original_list[k+1],original_list[k]
print("The sorted list is:",original_list)
print("The gratest number in the list is:",original_list[len(original_list)-1])

