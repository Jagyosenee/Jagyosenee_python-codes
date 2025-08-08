#Ask the user to input a sentence and a word. Write a program to check whether that word exists
# in the sentence or not.
sentence=input("Enter the sentence:")
word=input("Enter the word:")
if word not in sentence:
    print(word,"is not there in the sentence:",sentence)
else:
    print(word,"is there in the sentence:",sentence)