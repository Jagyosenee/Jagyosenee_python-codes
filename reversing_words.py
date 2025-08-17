#Enter 10 words in a list and print each word in reverse order.
word_list=[]
for i in range(11):
    words=input("Enter the words:")
    word_list.append(words)
print("The list with the words are",word_list)
rev_word_list=[]
for elements in word_list:
    rev=elements[::-1]
    rev_word_list.append(rev)
print("The list with the words are",rev_word_list)
    