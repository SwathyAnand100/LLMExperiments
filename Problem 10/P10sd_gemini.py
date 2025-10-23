# Implement both encode_shift(s) and decode_shift(s) so that encoding shifts each lowercase letter by 5 and decoding shifts back by 5.
# After coding, check your functions with test cases such as 'abc', 'xyz', and an empty string.
# If decoding does not return the original string, debug your code, focusing on the character shifting and wrap-around logic, and describe your corrections.
# Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.


def encode_shift_gemini_sd_pass1(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 5) % 26 + ord('a'))
        else:
            result += c
    return result

def decode_shift_gemini_sd_pass1(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') - 5) % 26 + ord('a'))
        else:
            result += c
    return result

def encode_shift_gemini_sd_pass2(s):
    shift_dict = {chr(i): chr((i - ord('a') + 5) % 26 + ord('a')) for i in range(ord('a'), ord('z')+1)}
    return ''.join(shift_dict.get(c, c) for c in s)

def decode_shift_gemini_sd_pass2(s):
    shift_dict = {chr((i - ord('a') + 5) % 26 + ord('a')): chr(i) for i in range(ord('a'), ord('z')+1)}
    return ''.join(shift_dict.get(c, c) for c in s)

import string

def encode_shift_gemini_sd_pass3(s):
    letters = string.ascii_lowercase
    return ''.join(letters[(letters.index(c)+5) % 26] if c in letters else c for c in s)

def decode_shift_gemini_sd_pass3(s):
    letters = string.ascii_lowercase
    return ''.join(letters[(letters.index(c)-5) % 26] if c in letters else c for c in s)