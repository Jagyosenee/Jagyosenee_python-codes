#Write a program that finds the maximum and minimum elements in a tuple of integers without using 
# built-in max () or min ().
x=int(input("Enter the number of elements:"))
tuple=()
for i in range(1,x+1):
   elements=int(input("enter the numbers:"))
   tuple+=(elements,)
print("The tuple is:",tuple)
max_num=tuple[0]
min_num=tuple[0]
for item in tuple:
    if item>max_num:
        max_num=item
    if item<min_num:
        min_num=item
print("The maximum number", max_num)
print("The minimum number", min_num)
