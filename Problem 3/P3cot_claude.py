#Prompt:
# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes a string and returns a new string with all vowels removed.
# Vowels include both lowercase and uppercase letters: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
# The function should preserve all other characters, including consonants, spaces, and newlines.
# Consider how to handle empty strings and strings with no vowels.
# After explaining your reasoning, provide your Python function implementation.

def claude_cot_pass1(txt):
    vowels = "aeiouAEIOU"
    result = ""
    for char in txt:
        if char not in vowels:
            result += char
    return result

def claude_cot_pass2(txt):
    vowels = "aeiouAEIOU"
    return "".join([char for char in txt if char not in vowels])


def claude_cot_pass3(txt):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        txt = txt.replace(vowel, "")
    return txt
