#COT Prompt
# Explain step-by-step how you would solve the following problem:
# Create a function that takes txt as input parameter, and that returns True if the last character of a 
# given string is an alphabetical character and is not a part of a word, and False otherwise. 
# Remember, a "word" is a group of characters separated by space.
# After explaining your reasoning, provide your Python function implementation.

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


def claude_cot_pass1(txt):
    if not txt:
        return False
    
    # Split the string into words by spaces
    tokens = txt.split()
    
    # Edge case: no words after splitting (all spaces)
    if not tokens:
        return False
    
    # Take the last token
    last_token = tokens[-1]
    
    # Check if last token is a single alphabetical character
    return len(last_token) == 1 and last_token.isalpha()

def claude_cot_pass2(txt):
    if not txt:
        return False
    
    # Get the last "word" after the last space
    last_token = txt.rstrip().rsplit(' ', 1)[-1]
    
    # Check if it's a single alphabetical character
    return len(last_token) == 1 and last_token.isalpha()

def claude_cot_pass3(txt):
    if not txt:
        return False
    
    i = len(txt) - 1
    
    # Skip trailing spaces
    while i >= 0 and txt[i].isspace():
        i -= 1
    
    # Edge case: string had only spaces
    if i < 0:
        return False
    
    # Check if last non-space character is alphabetical
    if not txt[i].isalpha():
        return False
    
    # Check if it is standalone (either start of string or preceded by space)
    if i == 0 or txt[i-1].isspace():
        return True
    
    return False

#SD Prompt
# Write code for a function that takes txt as input parameter, and that returns True if the last 
# character of a given string is an alphabetical character and is not a part of a word, and False otherwise. 
# Remember, a "word" is a group of characters separated by space or punctuation. After implementing your initial solution, review 
# your approach by identifying any potential issues, edge cases, or mistakes.
#  Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, 
# corrected answer along with the code.

def gemini_sd_pass1(txt):
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # 2. Check if the last character is alphabetical
    if not last_char.isalpha():
        return False
        
    # 3. Handle single-character string (e.g., "A")
    if len(txt) == 1:
        return True
    
    # 4. Check the preceding character for word continuation
    prev_char = txt[-2]
    
    # If the previous character is also alphabetical, the last char is part of a 
    # word (e.g., "helloa").
    if prev_char.isalpha():
        return False
    else:
        # If the previous character is not alphabetical (space, punctuation, digit, etc.),
        # the last character starts a new word, making it an isolated word.
        # Examples: "word!a", "b a", "1a"
        return True


def gemini_sd_pass2(txt):
    import re
    # The pattern matches: 
    # (^)   Start of string 
    # OR    
    # ([^a-zA-Z]) A non-alphabetic character
    # followed by:
    # ([a-zA-Z]$) A single alphabetic character at the very end of the string
    pattern = r'(^|[^a-zA-Z])[a-zA-Z]$'
    
    # re.search returns a match object if the pattern is found, otherwise None.
    return bool(re.search(pattern, txt))

def gemini_sd_pass3(txt):
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # 1. Check if the last character is alphabetical
    if not last_char.isalpha():
        return False
        
    # 2. The isolation check: 
    #    The last char is isolated if:
    #    a) The string has length 1 (isolated by default).
    #    OR
    #    b) The character preceding it (txt[-2]) is NOT alphabetical.
    
    if len(txt) == 1:
        return True
    
    # Check if the character before the last one is non-alphabetic
    # If it is non-alphabetic, the last char is isolated.
    return not txt[-2].isalpha()


def claude_sd_pass1_failed(txt): #fails when single letter is passed
    # Edge case: empty string
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # Check if last character is alphabetical
    if not last_char.isalpha():
        return False
    
    # Edge case: single character string
    # A single letter could be considered a word itself (like "I" or "a")
    # So it IS part of a word
    if len(txt) == 1:
        return False
    
    # Check the character before the last one
    second_to_last = txt[-2]
    
    # If preceded by space or non-alphanumeric (punctuation), 
    # the last character is isolated/standalone
    if second_to_last.isspace() or (not second_to_last.isalnum()):
        return True
    
    # If preceded by another alphanumeric character, it's part of a word
    return False

#prompt 2:
# Write code for a function that takes txt as input parameter, and that returns True if the last 
# # character of a given string is an alphabetical character and is not a part of a word, and False otherwise. 
# Remember, a "word" is a group of characters separated by space or punctuation. Note that a single letter is considered a letter only. not a word. 
# After implementing your initial solution, review
# your approach by identifying any potential issues, edge cases, or mistakes. # Debug your own solution, 
# correcting any flaws you find. Finally, state the rationale for your final, # corrected answer along with the code.
def claude_sd_pass1(txt):
    # Edge case: empty string
    if not txt:
        return False
    
    last_char = txt[-1]
    
    # Check if last character is alphabetical
    if not last_char.isalpha():
        return False
    
    # Edge case: single character string
    # A single letter is considered a letter only, NOT a word
    if len(txt) == 1:
        return True
    
    # Check the character before the last one
    second_to_last = txt[-2]
    
    # If preceded by space or non-alphanumeric (punctuation), 
    # the last character is a standalone letter (not part of a word)
    if second_to_last.isspace() or (not second_to_last.isalnum()):
        return True
    
    # If preceded by another alphanumeric character, it's part of a word
    return False

def claude_sd_pass2(txt):
    # Edge case: empty string
    if not txt:
        return False
    
    # Match a single letter at the end of the string
    # preceded by either start of string, space, or non-alphanumeric
    match = re.search(r'(^|[^a-zA-Z0-9])[a-zA-Z]$', txt)
    return bool(match)

def claude_sd_pass3(txt):
    # Edge case: empty string
    if not txt:
        return False
    
    # Split string by whitespace
    tokens = txt.split()
    
    if not tokens:
        return False
    
    # Check last token
    last_token = tokens[-1]
    
    # If last token is a single alphabetical character, it's standalone
    return len(last_token) == 1 and last_token.isalpha()
