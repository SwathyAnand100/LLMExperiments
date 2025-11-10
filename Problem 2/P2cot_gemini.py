#COT Prompt
# Explain step-by-step how you would solve the following problem:
# Create a function that takes txt as input parameter, and that returns True if the last character of a 
# given string is an alphabetical character and is not a part of a word, and False otherwise. 
# Remember, a "word" is a group of characters separated by space.
# After explaining your reasoning, provide your Python function implementation.

#COT Prompt2:
# Task: Write a function that accepts a string txt and returns True if the string’s last character is a letter that does not belong to a word, and False otherwise. A “word” is defined as a sequence of characters separated by spaces.Instructions:
# Think through how to identify the last character of the string.
# Consider how to determine whether this character is alphabetical.
# Analyze how to check if it is part of a word or stands alone.
# After reasoning through the approach step by step, implement the Python function that performs this check.


def gemini_cot_pass1(txt):
    """
    Returns True if the last character of a string is an alphabetical character 
    and is not part of a word, and False otherwise.
    """
    
    # Must have at least one character.
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # Must be alphabetical.
    if not last_char.isalpha():
        return False
    
    # Must either be the only character OR be preceded by a space.
    # len(txt) == 1 handles the single-character case.
    # txt[-2] == ' ' handles the space-preceded case for strings > 1.
    return len(txt) == 1 or txt[-2] == ' '

def gemini_cot_pass2(txt):
    """
    Alternative 1: Uses string slicing and the isalpha() check on the last char.
    """
    # 1. Check for empty string
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # 2. Check if alphabetical
    if not last_char.isalpha():
        return False
        
    # 3. Check for 'not part of a word' condition
    
    # If the string has only one character, the condition is met.
    if len(txt) == 1:
        return True
        
    # If the string has more than one character, check if the string 
    # (excluding the last character) ends with a space.
    # txt[:-1] is the slice containing all characters up to, but not including, the last one.
    return txt[:-1].endswith(' ')

import re

def gemini_cot_pass3(txt):   
    # Simplified Pattern: (.* \s*[a-zA-Z])|(^[a-zA-Z]$)
    
    # Simpler pattern focusing only on the end of the string:
    # (.* \s*[a-zA-Z]$)|(^[a-zA-Z]$)
    
    pattern = r"^(.* \s*[a-zA-Z]| [a-zA-Z])|[a-zA-Z]$"
    
    # Let's use a cleaner pattern:
    # 1. Matches: "anything" + "space" + "letter" (at the end)
    # 2. OR Matches: "single letter"
    pattern = r"^(.* \s*[a-zA-Z]|[a-zA-Z])$"
    
    # Final, most concise regex for the condition:
    # (.* \s*[a-zA-Z]$) -> Preceded by space
    # (^[a-zA-Z]$) -> Single character
    pattern = r"(^.* \s*[a-zA-Z]$)|(^[a-zA-Z]$)"
    
    # re.match checks if the pattern matches at the beginning of the string.
    # Since we use ^ (start) and $ (end), it ensures the *entire* string matches the criteria.
    return bool(re.match(pattern, txt))
