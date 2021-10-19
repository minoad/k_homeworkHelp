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
first_name_unit_tests_dict: list[dict] = [
    {
        "testname": "First Name process",
        "test_content": "Korra",
        "expected_return": "K",
        "expect_error": False
    },
    {
        "testname": "One letter",
        "test_content": "Z",
        "expected_return": "",
        "expect_error": False
    },
    {
        "testname": "No consonants after the first letter",
        "test_content": "Poaeeoau",
        "expected_return": "",
        "expect_error": False
    },
    {
        "testname": "Empty string",
        "test_content": "",
        "expected_return": "",
        "expect_error": False
    },
    {
        "testname": "No Consonants at all",
        "test_content": "ooaaeeiio",
        "expected_return": "",
        "expect_error": False
    },
    {
        "testname": "Two letters, no vowels",
        "test_content": "JP",
        "expected_return": "JP",
        "expect_error": False
    },
    {
        "testname": "First Name process standard",
        "test_content": "Aaron",
        "expected_return": "Aar",
        "expect_error": False
    },
]

## Unit tests in list form
# Did you get instrunction on what to print in case of an edge case.  I am assuming just print a blank line which is what i have done.
first_name_unit_tests_list: list[str] = [
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

# Running the tests using the list method.
# for test in first_name_unit_tests_list:
#     print(matching_to_first_consonent(test))

# Run the tests using the dict.  Using this method you can automaically check the results.  
# Can have thousands of tests in here and only look at a result where result != expected result.
# Here is an element of the list of dicts.
    # {
    #     "testname": "No consonants after the first letter",
    #     "test_content": "Poaeeoau",
    #     "expected_return": "",
    #     "expect_error": False
    # },
# for test in first_name_unit_tests_dict:
#     print(matching_to_first_consonent(test["test_content"]))
for test in first_name_unit_tests_dict:
    content: str = test["test_content"] # looks like a bug in the linter for type hinting.
    print(f'test {test["testname"]} - success: {test["expected_return"] == matching_to_first_consonent(content)}. Returned result of {matching_to_first_consonent(content)} compared to expectation of {test["expected_return"]}.')
    #print(matching_to_first_consonent(content))
