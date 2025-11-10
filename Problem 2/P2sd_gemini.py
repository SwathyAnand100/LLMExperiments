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