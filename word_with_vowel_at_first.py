# WAP to enter a sentence and bring every word that starts with a vowel to the first of the list and
# sort in "a e i o u".
sentence=input("Enter a sentence:")
words_starting_with_vowels=[]
words_starting_with_consonants=[]
vowel="AEIOUaeiou"
words=sentence.split()

for i in words:
    if i[0] in vowel:
        words_starting_with_vowels.append(i)
    else:
        words_starting_with_consonants.append(i)   
        
print("List with words starting with vowels is:",words_starting_with_vowels)
print("List with words starting with consonants is:",words_starting_with_consonants)

vowel_order = ["a", "e", "i", "o", "u"]

sorted_vowels_word = []
for v in vowel_order:
    for word in words_starting_with_vowels:
        if word[0] == v:   
            sorted_vowels_word.append(word)

print("Sorted list of words starting with vowels:", sorted_vowels_word) 

final_list=sorted_vowels_word+words_starting_with_consonants
print("The sorted list with vowels at first then consonent is:",final_list)