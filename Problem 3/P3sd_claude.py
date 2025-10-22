#Write code for a function that takes a string and returns a new string with all vowels removed.
# Vowels include both lowercase and uppercase letters: 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
# The function should preserve all other characters, including consonants, spaces, and newlines.
# Consider how to handle empty strings and strings with no vowels. 
# After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes.
#  Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.

def claude_sd_pass1(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def claude_sd_pass2(text):
    vowels = "aeiouAEIOU"
    return "".join([char for char in text if char not in vowels])


def claude_sd_pass3(text):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text
