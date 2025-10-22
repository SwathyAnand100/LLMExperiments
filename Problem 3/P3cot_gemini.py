# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string and returns a new string with all vowels removed.
# Vowels include both lowercase and uppercase letters: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
# The function should preserve all other characters, including consonants, spaces, and newlines.
# Consider how to handle empty strings and strings with no vowels.
# After explaining your reasoning, provide your Python function implementation.

def gemini_cot_pass1(txt):
    # 1. Define the Vowel Set for efficient lookup (O(1) average time complexity)
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # 4. Initialize an empty list to build the new string
    result_chars = []

    # 2. Iterate through the input string
    for char in txt:
        # 3. Check for Vowels
        # 4. If the character is NOT a vowel, append it to the result list
        if char not in VOWELS:
            result_chars.append(char)

    # 6. Join the characters back into a single string and return
    return "".join(result_chars)

def gemini_cot_pass2(txt):
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Use a list comprehension to build a list of characters 
    # that are NOT in the VOWELS set, then join them into a string.
    return "".join([char for char in txt if char not in VOWELS])


def gemini_cot_pass3(txt):
    vowels_to_remove = 'aeiouAEIOU'
    # 1. Create a translation table
    # This table maps each vowel character to None, indicating it should be deleted.
    # The str.maketrans() function is used for this.
    translation_table = str.maketrans('', '', vowels_to_remove)
    
    # 2. Apply the translation table to the input string
    return txt.translate(translation_table)