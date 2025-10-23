# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string of words separated by commas or spaces and returns a list of the words.
# Consider how to handle cases where words are separated by spaces, commas, or both.
# Think about how to deal with extra spaces, multiple commas, or combinations of delimiters.
# Consider edge cases such as empty strings or strings with only delimiters.
# After explaining your reasoning, provide your Python function implementation.

import re
from typing import List

def gemini_cot_pass1(text: str) -> List[str]:    
    # Check for empty string input immediately to handle this edge case gracefully
    if not text:
        return []

    # Regular Expression Pattern: Matches one or more occurrences of a comma (,) or a whitespace character (\s).
    # This pattern treats ', ', '  ', and ' , ' as a single delimiter.
    delimiter_pattern = r'[,\s]+'
    
    # 1. Split the text using the comprehensive delimiter pattern.
    # This may result in empty strings ('') in the list.
    word_list = re.split(delimiter_pattern, text)
    
    # 2. Filter the list to remove all empty strings that result from 
    # leading/trailing delimiters or multiple consecutive delimiters.
    # The condition 'if word' checks if the string is non-empty.
    # This handles edge cases like " , , " or "" gracefully.
    cleaned_words = [word for word in word_list if word]
    
    return cleaned_words

def gemini_cot_pass2(text:str) -> List[str]:
    #from typing import List
    if not text:
        return []

    # 1. Replace all commas with a single space.
    # e.g., "apple,banana orange" -> "apple banana orange"
    normalized_text = text.replace(',', ' ')
    
    # 2. Use str.split() without arguments. 
    # This automatically splits on ANY sequence of whitespace (single space, 
    # multiple spaces, tabs, etc.) and crucially filters out empty strings.
    # e.g., "apple  banana" -> ['apple', 'banana']
    
    return normalized_text.split()

def gemini_cot_pass3(text:str) -> List[str]:
    if not text:
        return []

    # 1. Choose a unique delimiter not expected to be in the input words.
    CANONICAL_DELIMITER = '|'
    
    # 2. Normalize the string: Replace all commas with the canonical delimiter.
    temp_text = text.replace(',', CANONICAL_DELIMITER)
    
    # 3. Normalize remaining spaces (and any runs of delimiters) with the canonical delimiter.
    # Note: Using replace(' ', '|') here can create multiple '|' characters if there were runs of spaces,
    # which we handle by filtering the resulting list later.
    final_text = temp_text.replace(' ', CANONICAL_DELIMITER)
    
    # 4. Split the text explicitly on the canonical delimiter.
    word_list = final_text.split(CANONICAL_DELIMITER)
    
    # 5. Filter out empty strings that resulted from leading/trailing delimiters 
    # or runs of multiple delimiters (e.g., "word,  word" -> "word|||word").
    return [word for word in word_list if word]
