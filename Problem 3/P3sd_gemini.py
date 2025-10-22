#Write code for a function that takes a string and returns a new string with all vowels removed.
# Vowels include both lowercase and uppercase letters: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
# The function should preserve all other characters, including consonants, spaces, and newlines.
# Consider how to handle empty strings and strings with no vowels. 
# After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes.
#  Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.

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