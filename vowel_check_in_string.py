#Write a program that counts how many vowels are present in a user-provided string.
str=input("Enter the string:")
vowel= "AEIOUaeiou"
count=0
for i in str:
    if i in vowel:
       count+=1
print("The number of vowels in the string is",count)
    