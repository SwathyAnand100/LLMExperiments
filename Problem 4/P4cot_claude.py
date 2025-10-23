# Task: Write a function that accepts a string and calculates the sum of ASCII values of only the uppercase letters ('A' through 'Z'). If the string is empty or contains no uppercase letters, the function should return 0. Instructions:
# Think step by step about how to identify which characters in the string are uppercase.
# Consider how to compute and accumulate the ASCII values of these characters.
# Reflect on edge cases, such as an empty string or a string with no uppercase letters.
# After reasoning through your approach, write the Python function implementing the solution.


def claude_cot_pass1(text):
    total = 0
    for char in text:
        if 'A' <= char <= 'Z':  # or char.isupper()
            total += ord(char)
    return total
    
def claude_cot_pass2(text):
    return sum([ord(char) for char in text if char.isupper()])    
        
def claude_cot_pass3(text):
    return sum(map(ord, filter(str.isupper, text)))