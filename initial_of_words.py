# Enter a sentence and print the initials of each word.
sentence=input("Enter the sentence:")
words=sentence.split()
for word in words:
    print(word[0])