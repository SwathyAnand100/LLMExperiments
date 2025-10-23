# Task: Write a function that accepts a string and returns a version of the string with all vowels removed. Both uppercase and lowercase vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') should be excluded, while all other characters,including consonants, spaces, punctuation, and newlines, remain unchanged.Instructions:
# Think step by step about how to identify vowels in the string.
# Consider different ways to construct a new string without vowels (e.g., iteration, list comprehension, or built-in functions).
# Take into account special cases, such as empty strings or strings that contain no vowels.
# After reasoning through your approach, write the Python function implementing your solution.


def gemini_sd_pass1(input_string):
    VOWELS = "aeiouAEIOU"
    
    # Initialize a list to store non-vowel characters. 
    # This is much more efficient than repeated string concatenation.
    non_vowel_chars = []
    
    # Iterate over the input string character by character
    for char in input_string:
        # Check if the character is NOT in the defined set of vowels
        if char not in VOWELS:
            non_vowel_chars.append(char)
            
    # Join the collected list of characters into a single string and return it
    return "".join(non_vowel_chars)

def gemini_sd_pass2(input_string):
    VOWELS = "aeiouAEIOU"
    non_vowel_chars = [char for char in input_string if char not in VOWELS]
    return "".join(non_vowel_chars)

def gemini_sd_pass3(input_string):
    import re
    return re.sub(r'[aeiou]', '', input_string, flags=re.IGNORECASE)