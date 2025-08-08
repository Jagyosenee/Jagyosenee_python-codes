#Write a program to check if a given string is a palindrome (same forward and backward).
str=input("Enter a string:")
rev_of_str=str[::-1]
if str==rev_of_str:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

