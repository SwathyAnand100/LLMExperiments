import re

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
