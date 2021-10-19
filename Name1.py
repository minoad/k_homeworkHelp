#Couple Name Generator
#Kaitlin Regan

'''
Assignment criteria
For the first name: Ignore the first letter, then find the first consonant and 
keep everything before and including the first consonant.

For the second name: If it starts with a vowel, keep the whole second name. 
If it starts with a consonant, keep every letter after the first consonant, but not including it. 

Only the first letter in the couple name should be capitalized

Examples: "Korra" and then "Asami" would be "Korasami"
          "Jim" and then "Pam" would be "Jimam"

I am working on the code with the names as values I set in order to test it
before changing the values to user input statements
'''          

consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel = "aeiouAEIOU"

name_1 = "Korrza"
name_2 = "Asami"

#it had been printing the intended output prior to this morning, although it was printing it twice.
#today I'm not getting any output. Not sure what changed

for i, character in enumerate(name_1):
    if i != 0:
        if character in consonant:
            name_1 = name_1[0:i+1]
            print(f'on character {character}, name: {name_1}')
            
for i, character in enumerate(name_2):
    if i != 0:
        if character in consonant:
            name_1 = name_1[0:i+1]
            print(f'on character {character}, name: {name_1}')
            

def imafunction(athingToDoStuffTo):
    
    return athingToDoStuffTo


