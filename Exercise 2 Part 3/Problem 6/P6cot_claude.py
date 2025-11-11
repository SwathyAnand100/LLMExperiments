# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string of words separated by commas or spaces and returns a list of the words.
# Consider how to handle cases where words are separated by spaces, commas, or both.
# Think about how to deal with extra spaces, multiple commas, or combinations of delimiters.
# Consider edge cases such as empty strings or strings with only delimiters.
# After explaining your reasoning, provide your Python function implementation.

def claude_cot_pass1(s):
    if s is None:
        return []
    # Turn commas into spaces, then split on any whitespace (split() collapses runs).
    # This also trims leading/trailing whitespace and discards empty tokens.
    return s.replace(',', ' ').split(' ') #BUG - using split(' ') keeps empty tokens instead of collapsing whitespace like split() does

import re
def claude_cot_pass2(s):
    if s is None:
        return []
    # split on runs of commas or whitespace
    parts = re.split(r'[, \t\n\r\f\v]+', s.strip())
    # re.split can produce [''] if the stripped string is empty, so filter empties
    return [p for p in parts if p]

def claude_cot_pass3(s):
    if not s:
        return []
    # Find all substrings that are not commas or whitespace
    return re.findall(r'[^,\s]+', s)