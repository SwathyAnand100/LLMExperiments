# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.
# Uppercase characters are 'A' to 'Z'.
# If the string is empty or contains no uppercase letters, return 0.
# Consider how to identify uppercase characters and how to sum their ASCII values.
# After explaining your reasoning, provide your Python function implementation.

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