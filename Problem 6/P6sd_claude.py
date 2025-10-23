# Task: Create a function that takes a string containing words separated by commas, spaces, or both, and returns a list of those words. Instructions:
# Think step by step about how to handle different types of delimiters such as spaces, commas, or their combinations.
# Consider how to manage cases with extra spaces, multiple commas in a row, or mixed delimiters.
# Reflect on how to treat edge cases, including empty strings or strings containing only delimiters.
# After implementing your initial approach, review your code to identify possible issues, mistakes, or unhandled edge cases.
# Debug and refine your solution to correct any flaws.
# Finally, explain the reasoning behind your corrected approach and provide the final Python function implementation.

import re
def claude_sd_pass1(s: str) -> list[str]:
    words = re.split(r'[,\s]+', s.strip())
    # Remove empty strings (can occur with edge cases)
    return [word for word in words if word]

def claude_sd_pass2(s: str) -> list[str]:
    result = []
    current = ""
    for ch in s:
        if ch not in [',', ' ']:
            current += ch
        else:
            if current:
                result.append(current)
                current = ""
    if current:
        result.append(current)
    return result

def claude_sd_pass3(s: str) -> list[str]:
    words = s.replace(',', ' ').split()
    return words