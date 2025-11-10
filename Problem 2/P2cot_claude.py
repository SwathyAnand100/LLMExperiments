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
