# Assignment criteria
# For the first name: Ignore the first letter, then find the first consonant and 
# keep everything before and including the first consonant.

# For the second name: If it starts with a vowel, keep the whole second name. 
# If it starts with a consonant, keep every letter after the first consonant, but not including it. 

# Set Constants
CONSONANT: str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
VOWEL: str = "aeiouAEIOU"
DEBUG: bool = False

# Set Unit Test
## I am not sure if you have done dicts yet, but this would usually be a list of dicts in the form of the following.
unit_tests: list[dict] = [
    {
        "testname": "First Name process",
        "test_content": "Korra",
        "expected_return": "K",
        "expect_error": False
     }    
]

## Im going to proceed with this method though.  Just a list of the test content.
first_name_test_cases: list[str] = [
    "Korra",
    "K", # edge case, only 1 char
    "Koaeeoau", # edge case no subsequent consonants
    "", # edge case empty name
    "ooaaeeiio" # edge case: no consonants

]

'''
    parse_first_name takes a string, drops the first letter.  It then scans to the point of the first consonant and using that index number returns the input string from 0 to that index number + 1
'''
# Since i am not doing exception handling i am breaking this up into 2 functions.
## With exception handling, this can all be done on a single line of code but would be much less readable.
def parse_first_name(n: str)-> str:
    # Accept n=Korra.
    # Drop first letter. n[1:]
    # For n[n_idx+1]
        # if n[n_idx+1] in CONSONANT
        # return n_consonant_index
    # return n[0:(n_consonant_index+1)]
    print(get_index_of_first_consonant(n)+1)
    return f"{n[0]}{n[1:(get_index_of_first_consonant(n)+2)]}" # returns the `first letter in variable n` + all letters from the second letter in n up to and including the first consonant.

def get_index_of_first_consonant(n: str) -> int:
    # Would usually do this with exception handling, but you might not be there yet.
    err_val: int = -1 # if err_val is returned, something unexpected has happened.
    for c in enumerate(n[1:]):
        if c[1] in CONSONANT:
            return c[0] 
    return err_val

n = parse_first_name(first_name_test_cases[0])
print(n)





# second_name:str = "Asami"



# def parse_second_name(n: str)-> str:
#     return("done second")