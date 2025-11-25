# test_spec_guided_P10.py
# Spec-guided tests for encode_shift / decode_shift based on
# formal assertions from Exercise 3 (Problem 10).

import pytest

from P10sd_gemini import (     # TODO: replace with actual file/module name
    encode_shift_gemini_sd_pass1,
    decode_shift_gemini_sd_pass1,
    encode_shift_gemini_sd_pass2,
    decode_shift_gemini_sd_pass2,
    encode_shift_gemini_sd_pass3,
    decode_shift_gemini_sd_pass3,
)

ENCODERS = [
    encode_shift_gemini_sd_pass1,
    encode_shift_gemini_sd_pass2,
    encode_shift_gemini_sd_pass3,
]

DECODERS = [
    decode_shift_gemini_sd_pass1,
    decode_shift_gemini_sd_pass2,
    decode_shift_gemini_sd_pass3,
]

# ----------------------------------------------------------
# Helper: compute expected encode (shift +5 modulo 26)
# ----------------------------------------------------------

def expected_encode(s: str) -> str:
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += chr(((ord(c) - ord('a') + 5) % 26) + ord('a'))
        else:
            res += c
    return res

# Helper: compute expected decode (shift -5 modulo 26)
def expected_decode(s: str) -> str:
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += chr(((ord(c) - ord('a') - 5) % 26) + ord('a'))
        else:
            res += c
    return res


# ----------------------------------------------------------
# SPEC-GUIDED TESTS FOR encode_shift
# ----------------------------------------------------------

@pytest.mark.parametrize("encoder", ENCODERS, ids=["enc1", "enc2", "enc3"])
@pytest.mark.parametrize("s", [
    "",                     # empty
    "abc",                  # basic shift
    "xyz",                  # wraparound
    "hello",                # normal lowercase
    "a",                    # single char
    "a1b!c",                # mixed chars (non-lowercase unchanged)
])
def test_spec_guided_encode_shift(encoder, s):
    """
    Spec-guided: tests correspond directly to assertions 1–4.
    """
    res_enc = encoder(s)

    alphabetic_lower_s = all('a' <= c <= 'z' for c in s)

    # 1. Length preserved
    assert len(res_enc) == len(s)

    # 2. Output lowercase only if input lowercase
    if alphabetic_lower_s:
        assert all('a' <= c <= 'z' for c in res_enc)

    # 3. +5 shift mod 26 on lowercase chars
    if alphabetic_lower_s:
        expected = expected_encode(s)
        assert res_enc == expected

    # 4. Empty case
    if s == "":
        assert res_enc == ""


# ----------------------------------------------------------
# SPEC-GUIDED TESTS FOR decode_shift
# ----------------------------------------------------------

@pytest.mark.parametrize("decoder", DECODERS, ids=["dec1", "dec2", "dec3"])
@pytest.mark.parametrize("encoded", [
    "",             # empty
    "fgh",          # encoded "abc"
    "cde",          # encoded "xyz"
    "mjqqt",        # encoded "hello"
    "f",            # encoded "a"
    "f1g!h",        # mixed
])
def test_spec_guided_decode_shift(decoder, encoded):
    """
    Spec-guided: tests correspond to assertions 6–8.
    """
    res_dec = decoder(encoded)

    alphabetic_lower_encoded = all('a' <= c <= 'z' for c in encoded)

    # 6. Length preserved
    assert len(res_dec) == len(encoded)

    # 7. decode reverses +5 shift
    if alphabetic_lower_encoded:
        expected = expected_decode(encoded)
        assert res_dec == expected

    # 8. Empty case
    if encoded == "":
        assert res_dec == ""


# ----------------------------------------------------------
# ROUND-TRIP SPEC-CONSISTENCY TESTS
# decode_shift(encode_shift(s)) == s
# ----------------------------------------------------------

@pytest.mark.parametrize("encoder,decoder", [
    (encode_shift_gemini_sd_pass1, decode_shift_gemini_sd_pass1),
    (encode_shift_gemini_sd_pass2, decode_shift_gemini_sd_pass2),
    (encode_shift_gemini_sd_pass3, decode_shift_gemini_sd_pass3),
])
@pytest.mark.parametrize("s", [
    "",
    "abc",
    "xyz",
    "hello",
    "testcase",
])
def test_spec_guided_round_trip(encoder, decoder, s):
    """
    Spec-guided: decoding an encoded string must return the original.
    """
    res_enc = encoder(s)
    res_dec = decoder(res_enc)
    assert res_dec == s
