# Task: Implement a function that takes a string and returns the sum of ASCII values of uppercase letters only ('A'–'Z'). If the string is empty or has no uppercase letters, it should return 0.Instructions:
# Reason through your initial approach step by step, thinking about how to identify uppercase characters and calculate their ASCII sum.
# Consider potential issues, edge cases, or mistakes in your approach.
# Debug your solution, making any necessary corrections.
# Explain the rationale for your final method and provide the corrected Python function implementation.



def claude_sd_pass1(s):
    total = 0
    for char in s:
        if char.isupper():  # Check if character is uppercase
            total += ord(char)
    return total

def claude_sd_pass2(s):
    return sum(ord(char) for char in s if 'A' <= char <= 'Z')

def claude_sd_pass3(s):
    uppercase_chars = filter(lambda c: 'A' <= c <= 'Z', s)
    return sum(map(ord, uppercase_chars))
