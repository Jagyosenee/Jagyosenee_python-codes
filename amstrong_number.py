# Enter a number and print if it is an Armstrong number or not.
n=int(input("Enter the number:"))
number=n
count_of_digits=0
while n!=0:
    n = n//10
    count_of_digits+=1
print("The number of digits in the number is:",count_of_digits)
copy_of_the_number=number
sum_of_the_digits=0
while number>0:
    digit=0
    digit=number%10
    sum_of_the_digits+=digit**count_of_digits
    number=number//10
if sum_of_the_digits == copy_of_the_number:
    print(copy_of_the_number,"is a amstrong number")
else:
    print(copy_of_the_number,"is not a amstrong number")
    