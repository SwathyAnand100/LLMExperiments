# Write code for a function that takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.
# Uppercase characters are 'A' to 'Z'.
# If the string is empty or contains no uppercase letters, return 0.
# Consider how to identify uppercase characters and how to sum their ASCII values. 
# After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes.
#  Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code. 

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
