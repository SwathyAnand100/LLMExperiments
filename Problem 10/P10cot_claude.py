#Generate 2 functions encode_shift and decode_shift: For encoding, describe how each lowercase letter is shifted forward by 5 positions 
# in the alphabet, wrapping around from 'z' to 'a' if necessary.
# For decoding, explain how to reverse the process by shifting each character backward by 5 positions, again handling wrap-around.
# Consider how to process only lowercase letters and what to do with other characters.
# Before coding, break down the problem:
# How does the encoding function transform each character in the string?
# What mathematical operation will undo this transformation for decoding?
# How will you handle wrap-around for letters near the start or end of the alphabet?
# Should you process only lowercase letters, or all characters?
# Write out your reasoning, then implement both the encoding and decoding functions.
def encode_shift_claude_cot_pass1(text):
    """Shift lowercase letters forward by 5 positions, wrap around 'z' -> 'a'."""
    result = []
    for c in text:
        if 'a' <= c <= 'z':
            shifted = (ord(c) - ord('a') + 5) % 26
            result.append(chr(shifted + ord('a')))
        else:
            result.append(c)
    return ''.join(result)


def decode_shift_claude_cot_pass1(text):
    """Shift lowercase letters backward by 5 positions, wrap around 'a' -> 'z'."""
    result = []
    for c in text:
        if 'a' <= c <= 'z':
            shifted = (ord(c) - ord('a') - 5) % 26
            result.append(chr(shifted + ord('a')))
        else:
            result.append(c)
    return ''.join(result)

import string

def encode_shift_claude_cot_pass2(text):
    letters = string.ascii_lowercase
    shifted = letters[5:] + letters[:5]  # 'fghijklmnopqrstuvwxyzabcde'
    trans = str.maketrans(letters, shifted)
    return text.translate(trans)

def decode_shift_claude_cot_pass2(text):
    letters = string.ascii_lowercase
    shifted = letters[5:] + letters[:5]
    trans = str.maketrans(shifted, letters)
    return text.translate(trans)

def encode_shift_claude_cot_pass3(text):
    return ''.join(
        chr((ord(c) - ord('a') + 5) % 26 + ord('a')) if 'a' <= c <= 'z' else c
        for c in text
    )

def decode_shift_claude_cot_pass3(text):
    return ''.join(
        chr((ord(c) - ord('a') - 5) % 26 + ord('a')) if 'a' <= c <= 'z' else c
        for c in text
    )