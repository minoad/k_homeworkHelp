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
# I am not sure if you have done dicts yet, but this would usually be a list of dicts in the form of the following.
unit_tests: list[dict] = [
    {
        "testname": "First Name process",
        "test_content": "Korra",
        "expected_return": "K",
        "expect_error": False
    }
]

# Im going to proceed with this method though.  Just a list of the test content.
# Did you get instrunction on what to print in case of an edge case.  I am assuming just print a blank line which is what i have done.
first_name_test_cases: list[str] = [
    "Korra",  # Expect: Kor,
    "Z",  # Expect: '', edge case, only 1 char.
    "Poaeeoau",  # Expect: '', edge case no subsequent consonants
    "",  # Expect: '', edge case empty name
    "ooaaeeiio",  # Expect: '', edge case: no consonants
    "JP",  # Expect: JP, No Vowel
    "Aaron"  # Expect: 'Aar', normal case

]

'''
    matching_to_first_consonent takes a string, drops the first letter.  It then scans to the point of the first consonant and using that index number returns the input string from 0 to that index number + 1
'''


def matching_to_first_consonent(n: str) -> str:
    # Would usually do this with exception handling, but you might not be there yet.
    err_val: str = ""  # if err_val is returned, something unexpected has happened.
    for c in enumerate(n):
        if c[1] in CONSONANT and c[0] != 0:
            return n[0:c[0]+1]
    return err_val


# This is how you can run all of your test cases.
for test in first_name_test_cases:
    print(matching_to_first_consonent(test))


# second_name:str = "Asami"


# def parse_second_name(n: str)-> str:
#     return("done second")
