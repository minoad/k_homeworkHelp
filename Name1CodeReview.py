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





# for i, character in enumerate(name_1):
#     if i != 0:
#         if character in consonant:
#             name_1 = name_1[0:i+1]
#             print(name_1)  

############ My Quick Code review of what you already have here ###########
## Use type hinting.  If your prof knows his stuff this will impress him.
## Constants are usually all caps

# You have these both as lists, I would probably start them as strings.
    # Often, things like this will be read from a file so it is usually best to keep these as primitive as possible and then parse later.
    # If you do set them as lists, this would be the type hint in 3.9+ CONSANANT: list[str]
# There are 2 better ways to do this.
    #  regex 
        # match `re.compile(r'str', flags=re.IGNORECASE)`
    # string manipulation
        # x.tolower() = y.tolower()
## consonant = ["bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"]
## vowel = ["aeiouAEIOU"]

# Set Constants
CONSONANT: str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
VOWEL: str = "aeiouAEIOU"
DEBUG: bool = False

# Set Unit Test
name_1:str = "Korra"
name_2:str = "Asami"

for i, character in enumerate(name_1):
    # You are doing this to ignore the first letter.
    ##     if i != 0:
    # Start getting used to using fstrings even when you are just printing for debug purposes.
    # note the variable debug in the constants section.  Makes it very easy to add debug statements during dev and turn them on an off with a single variable.
    if DEBUG: print(f'{i} -- {character}')
    if character in list(CONSONANT):
        if DEBUG: print(f'{character}')
    # you are appending back onto the existing variable.
        # Not sure why you are not getting output, but im not really sure what you are trying to do here.  
        # This is the output if I stick this in the debugger. 
            # name_1: Korra -- name_1[0:i+1]: K
            # name_1: K -- name_1[0:i+1]: K
            # name_1: K -- name_1[0:i+1]: K
            # name_1: K -- name_1[0:i+1]: K
            # name_1: K -- name_1[0:i+1]: K
        #it had been printing the intended output prior to this morning, although it was printing it twice.
        #today I'm not getting any output. Not sure what changed
    print(f'name_1: {name_1} -- name_1[0:i+1]: {name_1[0:i+1]}')
    name_1 = name_1[0:i+1]

