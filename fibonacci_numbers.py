#Write a program to print all Fibonacci numbers less than 100 using a while loop.
first_number=0
second_number=1
while first_number<100:
    print(first_number,end=" ")
    first_number,second_number=second_number, second_number+first_number
  
