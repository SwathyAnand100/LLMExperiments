# Explain step-by-step how you would implement both encode_shift(s) and decode_shift(s) functions.
# For encoding, describe how each lowercase letter is shifted forward by 5 positions in the alphabet, wrapping around from 'z' to 'a' if necessary.
# For decoding, explain how to reverse the process by shifting each character backward by 5 positions, again handling wrap-around.
# Consider how to process only lowercase letters and what to do with other characters.
# After your reasoning, provide both function implementations.
# --- Implementation 1: Ordinal Arithmetic ---

def encode_shift_geminicot_pass1(s: str) -> str:
    """Encodes by shifting lowercase letters forward by 5 (mod 26)."""
    A_ORD = ord('a')
    ALPHABET_SIZE = 26
    SHIFT = 5
    encoded_chars = []

    for char in s:
        if 'a' <= char <= 'z':
            original_index = ord(char) - A_ORD
            encoded_index = (original_index + SHIFT) % ALPHABET_SIZE
            encoded_chars.append(chr(encoded_index + A_ORD))
        else:
            encoded_chars.append(char)
            
    return "".join(encoded_chars)

def decode_shift_geminicot_pass1(s: str) -> str:
    """Decodes by shifting lowercase letters backward by 5 (mod 26)."""
    A_ORD = ord('a')
    ALPHABET_SIZE = 26
    DECODE_SHIFT = -5 # Inverse shift
    decoded_chars = []

    for char in s:
        if 'a' <= char <= 'z':
            original_index = ord(char) - A_ORD
            decoded_index = (original_index + DECODE_SHIFT) % ALPHABET_SIZE
            decoded_chars.append(chr(decoded_index + A_ORD))
        else:
            decoded_chars.append(char)
            
    return "".join(decoded_chars)

# --- Implementation 2: Alphabet Lookup ---
import string

def encode_shift_geminicot_pass2(s: str) -> str:
    """Encodes using alphabet string indexing (shift +5)."""
    alphabet = string.ascii_lowercase
    ALPHABET_SIZE = 26
    SHIFT = 5
    encoded_chars = []

    for char in s:
        if char in alphabet:
            original_index = alphabet.index(char)
            encoded_index = (original_index + SHIFT) % ALPHABET_SIZE
            encoded_chars.append(alphabet[encoded_index])
        else:
            encoded_chars.append(char)
            
    return "".join(encoded_chars)

def decode_shift_geminicot_pass2(s: str) -> str:
    """Decodes using alphabet string indexing (shift -5)."""
    alphabet = string.ascii_lowercase
    ALPHABET_SIZE = 26
    DECODE_SHIFT = -5
    decoded_chars = []

    for char in s:
        if char in alphabet:
            original_index = alphabet.index(char)
            decoded_index = (original_index + DECODE_SHIFT) % ALPHABET_SIZE
            decoded_chars.append(alphabet[decoded_index])
        else:
            decoded_chars.append(char)
            
    return "".join(decoded_chars)

# --- Implementation 3: Translation Table ---
import string

def _create_shift_map(shift: int) -> dict:
    """Helper to create the translation table for a given shift."""
    alphabet = string.ascii_lowercase
    ALPHABET_SIZE = 26
    
    # 1. Define the 'to' string by calculating the new position for each character
    to_chars = []
    for i in range(ALPHABET_SIZE):
        target_index = (i + shift) % ALPHABET_SIZE
        to_chars.append(alphabet[target_index])
        
    # 2. Create the translation table
    return str.maketrans(alphabet, "".join(to_chars))

# Pre-calculate tables (optimizing repeated calls)
ENCODE_TABLE = _create_shift_map(5)
DECODE_TABLE = _create_shift_map(-5)

def encode_shift_geminicot_pass3(s: str) -> str:
    """Encodes using a pre-calculated translation table (+5)."""
    return s.translate(ENCODE_TABLE)

def decode_shift_geminicot_pass3(s: str) -> str:
    """Decodes using a pre-calculated translation table (-5)."""
    return s.translate(DECODE_TABLE)