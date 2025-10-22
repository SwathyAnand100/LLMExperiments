# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.
# Uppercase characters are 'A' to 'Z'.
# If the string is empty or contains no uppercase letters, return 0.
# Consider how to identify uppercase characters and how to sum their ASCII values.
# After explaining your reasoning, provide your Python function implementation.

def gemini_cot_pass1(input_string):
    # 1. Initialize the running sum
    total_ascii_sum = 0
    
    # 2. Check for an empty string (Edge Case 1)
    if not input_string:
        return 0
    
    # 3. Iterate through the string character by character
    for char in input_string:
        # 4. Uppercase Character Identification
        # Check if the character is an uppercase letter ('A' through 'Z')
        if char.isupper():
            # 5. ASCII Value Calculation and Summation
            # Retrieve the ASCII code using ord() and add it to the total sum
            total_ascii_sum += ord(char)
            
    # 6. Return Value
    # This covers the case where the string has no uppercase letters (Edge Case 2), 
    # as the sum would remain 0.
    return total_ascii_sum


def gemini_cot_pass2(input_string):
    return sum(ord(char) for char in input_string if char.isupper())


def gemini_cot_pass3(input_string):
    total_ascii_sum = 0
    index = 0
    length = len(input_string)

    # Loop as long as the index is within the string bounds
    while index < length:
        char = input_string[index]
        
        # Identify and sum the uppercase character
        if char.isupper():
            total_ascii_sum += ord(char)
        
        # Move to the next character
        index += 1
        
    return total_ascii_sum