# Specifications for encode_shift

# Input and output variables:
# s: str        # input to encode_shift
# res_enc: str  # expected result of encode_shift(s)

alphabetic_lower_s = all('a' <= c <= 'z' for c in s)

# 1. Length is preserved by encoding
assert len(res_enc) == len(s)

# 2. If the input is all lowercase letters, the output is also all lowercase letters
if alphabetic_lower_s:
    assert all('a' <= c <= 'z' for c in res_enc)

# 3. For lowercase letters, each character is shifted by +5 (mod 26)
if alphabetic_lower_s:
    assert all(
        (ord(res_enc[i]) - ord('a')) ==
        ((ord(s[i]) - ord('a') + 5) % 26)
        for i in range(len(s))
    )

# 4. Encoding the empty string yields the empty string
if s == "":
    assert res_enc == ""

# 5. (INCORRECT SPECIFICATION – we will flag this later)
#    This claims the set of characters is unchanged, which is generally false
#    for a Caesar shift.
assert set(res_enc) == set(s)


# Specifications for decode_shift

# Input and output variables:
# encoded: str   # input to decode_shift
# res_dec: str   # expected result of decode_shift(encoded)

alphabetic_lower_encoded = all('a' <= c <= 'z' for c in encoded)

# 6. Length is preserved by decoding
assert len(res_dec) == len(encoded)

# 7. If the encoded text is all lowercase letters, decoding maps each
#    position back by -5 (i.e., res_dec shifted +5 gives encoded).
if alphabetic_lower_encoded:
    assert all(
        (ord(encoded[i]) - ord('a')) ==
        ((ord(res_dec[i]) - ord('a') + 5) % 26)
        for i in range(len(encoded))
    )

# 8. Decoding the empty string yields the empty string
if encoded == "":
    assert res_dec == ""