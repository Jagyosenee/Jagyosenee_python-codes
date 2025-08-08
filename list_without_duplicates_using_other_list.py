#Write a program that removes all duplicate elements from a list and prints the result.
x=int(input("Enter the number of terms:"))
original_list=[]
for i in range(0,x+1):
    a=int(input("Enter the elements:"))
    original_list.append(a)
print("The oiginal list is:",original_list)
list_without_duplicates=[]
for item in original_list:
    if item not in list_without_duplicates:
     list_without_duplicates.append(item)
print("List without duplicates is:",list_without_duplicates)

    
