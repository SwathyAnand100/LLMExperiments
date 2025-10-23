# Write code for a function that takes a string of words separated by commas or spaces and returns a list of the words.
# Consider how to handle cases where words are separated by spaces, commas, or both.
# Think about how to deal with extra spaces, multiple commas, or combinations of delimiters.
# Consider edge cases such as empty strings or strings with only delimiters.
# After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes. 
# Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.

import re
def gemini_sd_pass1(text: str) -> list[str]:
    if not isinstance(text, str):
        # Handle non-string input safely
        return []

    # 1. Normalize delimiters: Replace all commas with a single space.
    normalized_text = text.replace(',', ' ')
    
    # 2. Split by whitespace. 
    # Python's split() handles multiple spaces and leading/trailing whitespace
    # automatically, filtering out all empty tokens.
    words = normalized_text.split()
    
    return words

def gemini_sd_pass2(text: str) -> list[str]:
    if not isinstance(text, str) or not text:
        return []

    # Pattern: [\s,]+ matches one or more occurrences of either whitespace (\s) or a comma (,)
    words = re.split(r'[\s,]+', text)
    
    # re.split can sometimes return an empty string if the input starts/ends with 
    # the delimiter or is just delimiters. We must filter these out.
    # E.g., re.split(r'[\s,]+', ' , a , ') -> ['', 'a', '']
    # Filtering ensures only actual words are returned.
    return [word for word in words if word]

def gemini_sd_pass3(text: str) -> list[str]:
    if not isinstance(text, str):
        return []
    
    # 1. Normalize delimiters to spaces, handling consecutive delimiters by ensuring 
    # only one space is inserted for a run of delimiters.
    
    cleaned_text = []
    prev_char_was_delimiter = True # Initialize to True to suppress leading space if any
    
    for char in text:
        is_delimiter = char.isspace() or char == ','
        
        if is_delimiter:
            if not prev_char_was_delimiter:
                # Add a single space to separate words
                cleaned_text.append(' ')
                prev_char_was_delimiter = True
        else:
            # It's a non-delimiter character, add it and mark that we are inside a word
            cleaned_text.append(char)
            prev_char_was_delimiter = False
            
    # 2. Join the characters back into a string and use split() to handle any 
    # remaining leading/trailing spaces (if the last word wasn't followed by a space).
    # Since we suppressed leading delimiters and only added single spaces between words,
    # split() will handle the rest perfectly.
    return "".join(cleaned_text).split()
