'''
Name 2 portion
assignment criteria
For the second name: If it starts with a vowel, keep the whole second name. 
If it starts with a consonant, keep every letter after the first consonant, but not including it. 

This section was only working when set to a name beginning with a vowel
but it isn't anymore. Not sure what changed.
It hase never worked when set to a name beginning with a consonant. 
I've tried adjusting the indentation of the if statement
I've tried making it an else statement and tried with elif
I don't get an error: it won't print anything at all
'''

name_2 = "Evie"
vowel = ["aeiouAEIOU"]
consonant = ["bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"]

for i, character in enumerate(name_2):
    if i == 0:
        if character in vowel:
            name_2 = name_2
            print(name_2)
        
        if character in consonant:
            name_2 = name_2[1:i+1]
            print(name_2)
            