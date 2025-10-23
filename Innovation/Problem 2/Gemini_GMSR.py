#PROMPT:
# Create a Python function that checks if the last character of a given string is a letter (a–z or A–Z). 
# The function should return True if it is a letter, otherwise False.
# Examples:
# "Abc" -> True
# "abc!" -> False
# ""  -> False
# Agents and Roles:
# Planner - Explain how to handle different cases (empty strings, special characters, whitespace). Outline the logic clearly.
# Solver - Implement the function in clean, efficient Python code with inline comments explaining each step.
# Verifier - Design and run test cases including edge cases like empty strings, symbols, numbers, and mixed characters. Report any failures or inconsistencies.
# Refiner - Improve based on verifier feedback, ensuring robust handling of Unicode and whitespace, and produce the final clean implementation with a brief explanation.
# Goal:
# Deliver a function that is logically sound, handles all edge cases, and passes all verification tests.

import re

# --- Version 1 (Original Implementation: Most Pythonic) ---

def is_last_char_letter_v1(s: str) -> bool:
    """
    V1: Checks if the last character of a given string is an English letter (a-z or A-Z) 
    using the built-in .isalpha() method.

    :param s: The input string.
    :return: True if the last character is a letter, False otherwise.
    """
    # Step 1: Check for an empty string.
    if not s:
        return False

    # Step 2 & 3: Access last character and use .isalpha().
    return s[-1].isalpha()


# --- Version 2 (Alternative: Manual ASCII Range Check) ---

def is_last_char_letter_v2_ascii(s: str) -> bool:
    """
    V2: Checks if the last character is a letter by explicitly checking its 
    ASCII ordinal value against the ranges for 'a'-'z' and 'A'-'Z'.
    This is highly explicit for only English letters.

    :param s: The input string.
    :return: True if the last character is a letter, False otherwise.
    """
    if not s:
        return False

    last_char = s[-1]
    char_code = ord(last_char)

    # Check for uppercase letters (A=65 to Z=90)
    is_upper = (char_code >= ord('A')) and (char_code <= ord('Z'))
    
    # Check for lowercase letters (a=97 to z=122)
    is_lower = (char_code >= ord('a')) and (char_code <= ord('z'))

    return is_upper or is_lower


# --- Version 3 (Alternative: Regular Expression) ---

def is_last_char_letter_v3_regex(s: str) -> bool:
    """
    V3: Checks if the last character is a letter using a regular expression 
    pattern. The pattern '[a-zA-Z]$' ensures the last character matches 
    an English letter.

    :param s: The input string.
    :return: True if the last character is a letter, False otherwise.
    """
    # re.search() returns a match object (True) or None (False).
    # The pattern:
    # [a-zA-Z] - Matches any English letter (case-insensitive)
    # $        - Anchors the match to the very end of the string
    return bool(re.search(r'[a-zA-Z]$', s))

# --- Verification Test Cases (Examples for Demonstration) ---
if __name__ == '__main__':
    test_cases = {
        "Abc": True,
        "abc!": False,
        "": False,
        "TestZ": True,
        "999": False,
        "a": True,
        " ": False,
        "Hello World": True, # The last character is 'd'
        "test": True,
        "Last5": False
    }

    print("--- Running Verification Tests on All 3 Versions ---")
    
    # List of functions to test
    functions = [
        is_last_char_letter_v1, 
        is_last_char_letter_v2_ascii, 
        is_last_char_letter_v3_regex
    ]
    
    all_passed = True
    
    for func in functions:
        func_name = func.__name__
        print(f"\nTesting: {func_name}")
        
        for input_str, expected in test_cases.items():
            result = func(input_str)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"  Input: '{input_str}' -> Result: {result} ({status})")
            if status.startswith("FAIL"):
                all_passed = False
            
    if all_passed:
        print("\nAll versions passed all verification tests successfully!")
    else:
        print("\nSome tests failed in one or more versions. Review the implementations.")

