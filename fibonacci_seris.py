# Print the Fibonacci sequence up to n terms.
n=int(input("Enter the limit:"))
count=0
first_number=0
second_number=1
while count<n:
    print(first_number,end=" ")
    first_number,second_number=second_number, second_number+first_number
    count+=1