# Implement both encode_shift(s) and decode_shift(s) so that encoding shifts each lowercase letter by 5 and decoding shifts back by 5.
# After coding, check your functions with test cases such as 'abc', 'xyz', and an empty string.
# If decoding does not return the original string, debug your code, focusing on the character shifting and wrap-around logic, and describe your corrections.
# Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.


import string

SHIFT_AMOUNT = 5
ALPHABET_SIZE = 26
BASE_ASCII = ord('a')
ALPHABET = string.ascii_lowercase

def encode_shift_claude_sd_pass1(s: str) -> str:
    """
    Shifts each lowercase letter in the string 's' forward by 5 positions,
    wrapping from 'z' back to 'a'. Non-lowercase characters are unchanged.

    Args:
        s: The input string.

    Returns:
        The encoded string.
    """
    encoded_chars = []
    for char in s:
        if 'a' <= char <= 'z':
            # 1. Get the 0-indexed position (0 for 'a', 25 for 'z')
            current_pos = ord(char) - BASE_ASCII

            # 2. Apply the shift and use modulo for wrapping
            new_pos = (current_pos + SHIFT_AMOUNT) % ALPHABET_SIZE

            # 3. Convert the new position back to a character
            new_char = chr(new_pos + BASE_ASCII)
            encoded_chars.append(new_char)
        else:
            # Non-lowercase characters are appended unchanged
            encoded_chars.append(char)

    return "".join(encoded_chars)


def decode_shift_claude_sd_pass1(s: str) -> str:
    """
    Reverses the shift cipher by moving each lowercase letter in 's' backward
    by 5 positions, wrapping from 'a' back to 'z'. Non-lowercase characters
    are unchanged.

    Args:
        s: The encoded string.

    Returns:
        The decoded (original) string.
    """
    decoded_chars = []
    for char in s:
        if 'a' <= char <= 'z':
            # 1. Get the 0-indexed position (0 for 'a', 25 for 'z')
            current_pos = ord(char) - BASE_ASCII

            # 2. Apply the reverse shift. Python's % operator handles
            # negative results correctly for wrapping (e.g., -5 % 26 = 21).
            new_pos = (current_pos - SHIFT_AMOUNT) % ALPHABET_SIZE

            # 3. Convert the new position back to a character
            new_char = chr(new_pos + BASE_ASCII)
            decoded_chars.append(new_char)
        else:
            # Non-lowercase characters are appended unchanged
            decoded_chars.append(char)

    return "".join(decoded_chars)

def encode_shift_claude_sd_pass2(s: str) -> str:
    """
    V2: Shifts each lowercase letter using string indexing and modular arithmetic.
    """
    encoded_chars = []
    for char in s:
        if char in ALPHABET:
            current_index = ALPHABET.find(char)
            # Apply the shift and modulo
            new_index = (current_index + SHIFT_AMOUNT) % ALPHABET_SIZE
            encoded_chars.append(ALPHABET[new_index])
        else:
            encoded_chars.append(char)
    return "".join(encoded_chars)


def decode_shift_claude_sd_pass2(s: str) -> str:
    """
    V2: Reverses the shift using string indexing.
    """
    decoded_chars = []
    for char in s:
        if char in ALPHABET:
            current_index = ALPHABET.find(char)
            # Apply the reverse shift
            new_index = (current_index - SHIFT_AMOUNT) % ALPHABET_SIZE
            decoded_chars.append(ALPHABET[new_index])
        else:
            decoded_chars.append(char)
    return "".join(decoded_chars)

ENCODE_MAP = {}
DECODE_MAP = {}
for i in range(ALPHABET_SIZE):
    original_char = chr(i + BASE_ASCII)
    shifted_char = chr((i + SHIFT_AMOUNT) % ALPHABET_SIZE + BASE_ASCII)
    
    # Forward map for encoding
    ENCODE_MAP[original_char] = shifted_char
    # Reverse map for decoding
    DECODE_MAP[shifted_char] = original_char 

def encode_shift_claude_sd_pass3(s: str) -> str:
    """
    V3: Shifts the string using a pre-calculated dictionary lookup. 
    This is generally the fastest method for known shifts.
    """
    # .get(key, default) returns the mapped value, or the original char if not found
    return "".join(ENCODE_MAP.get(char, char) for char in s)

def decode_shift_claude_sd_pass3(s: str) -> str:
    """
    V3: Reverses the shift using a pre-calculated reverse dictionary lookup.
    """
    return "".join(DECODE_MAP.get(char, char) for char in s)


