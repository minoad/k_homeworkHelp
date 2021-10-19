# Set Constants
CONSONANT: str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
VOWEL: str = "aeiouAEIOU"
DEBUG: bool = False

name2UnitTestDict: list[dict] = [
    {
        "content": 114562,
        "name": "actual numbers",
        "expectedResult": ""
    },
    {
        "content": "",
        "name": "empty name",
        "expectedResult": ""
    },
        {
        "content": " ",
        "name": "space",
        "expectedResult": ""
    },
    {
        "content": "Aaron",
        "name": "Starts with vowel",
        "expectedResult": "Aaron",
    },
    {
        "content": "Billy",
        "name": "starts with cons",
        "expectedResult": "illy"
    },
    {
        "content": "Bieaaoopny",
        "name": "is a very long name",
        "expectedResult": "ieaaoopny"
    },
    {
        "content": "0155213",
        "name": "string of numbers",
        "expectedResult": ""
    },
]

# Expected result will be: Aaron, keep the whole second name
# Expected result will be : ['ly', 'lly'], Keep every letter after the first sonsonant but not including

# DONE: Expected result will be: Aaron, keep the whole second name
# DONE: Expected result will be : ['ly', 'lly'], Keep every letter after the first consonant but not including


def secondName(n: str) -> str:
    # Exception handling (this is not real exception handling)
    ## check we are a string and have at least 1 letter in it.
    if not isinstance(n, str) or len(n) == 0 or n == ' ': return ""

    # Case 1: starts with vowel
    if n[0] in VOWEL: return n

    # Case 2: starts with consonent
    for l in enumerate(n):
        # am i a consanent
        # If so forget me and return the remaining piece of the string.
        # 0,b; yes consanant; return b[idx] +1 to end.  illy
        if l[1] in CONSONANT:
            return n[l[0]+1:]

    # Case 3: we have encountered some errors stat and no return has run yet
    return ""

# ## Manual unit testing
# # expect Aaron
# print(
#     secondName(name2UnitTestDict[0]["content"])
#     )

# # expect illy
# print(secondName(name2UnitTestDict[1]["content"]))

#   {
#         "content": 114562,
#         "name": "actual numbers",
#         "expectedResult": ""
#     },


for test in name2UnitTestDict:
    print(f'{test["name"]}, -- {secondName(test["content"]) == test["expectedResult"]}')



def exe(n: str) -> str:
    if not isinstance(n, str) or len(n) == 0 or n == ' ': return ""
    if n[0] in VOWEL: return n
    
    for l in enumerate(n):
        if l[1] in CONSONANT:
            return n[l[0]+1:]

    return ""