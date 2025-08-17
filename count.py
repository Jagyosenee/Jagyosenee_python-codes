# Enter a sentence and print the count of vowel, consonants, special characters (., -;:?!)
sentence=input("Enter the sentence:")
space=" "
vowel="AEIOUaeiou"
special_character=".,-:;?!"
space_count=0
vowel_count=0
consonent_count=0
special_character_count=0

for i in sentence:
    if i in vowel:
        vowel_count+=1
    elif i==space:
        space_count+=1
    elif i in special_character:
        special_character_count+=1
    else:
        consonent_count+=1
print("The number of vowels are:",vowel_count)
print("The number of spaces are:",space_count)
print("The number of special characters are:",special_character_count)
print("The number of consonents are:",consonent_count)

        
        
    