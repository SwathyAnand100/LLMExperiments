#Prompt:
# Task: Write a function that accepts a string and returns a version of the string with all vowels removed. Both uppercase and lowercase vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') should be excluded, while all other characters,including consonants, spaces, punctuation, and newlines, remain unchanged.Instructions:
# Think step by step about how to identify vowels in the string.
# Consider different ways to construct a new string without vowels (e.g., iteration, list comprehension, or built-in functions).
# Take into account special cases, such as empty strings or strings that contain no vowels.
# After reasoning through your approach, write the Python function implementing your solution.


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
