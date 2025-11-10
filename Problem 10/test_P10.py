# from P10cot_gemini import encode_shift_geminicot_pass1
# from P10cot_gemini import encode_shift_geminicot_pass2
# from P10cot_gemini import encode_shift_geminicot_pass3
# from P10cot_gemini import decode_shift_geminicot_pass1
# from P10cot_gemini import decode_shift_geminicot_pass2
# from P10cot_gemini import decode_shift_geminicot_pass3

# from P10cot_claude import encode_shift_claude_cot_pass1
# from P10cot_claude import encode_shift_claude_cot_pass2
# from P10cot_claude import encode_shift_claude_cot_pass3
# from P10cot_claude import decode_shift_claude_cot_pass1
# from P10cot_claude import decode_shift_claude_cot_pass2
# from P10cot_claude import decode_shift_claude_cot_pass3

# from P10sd_claude import encode_shift_claude_sd_pass1
# from P10sd_claude import encode_shift_claude_sd_pass2
# from P10sd_claude import encode_shift_claude_sd_pass3
# from P10sd_claude import decode_shift_claude_sd_pass1
# from P10sd_claude import decode_shift_claude_sd_pass2
# from P10sd_claude import decode_shift_claude_sd_pass3

# from P10sd_gemini import encode_shift_gemini_sd_pass1
# from P10sd_gemini import encode_shift_gemini_sd_pass2
# from P10sd_gemini import encode_shift_gemini_sd_pass3
# from P10sd_gemini import decode_shift_gemini_sd_pass1
# from P10sd_gemini import decode_shift_gemini_sd_pass2
# from P10sd_gemini import decode_shift_gemini_sd_pass3

# def run_tests(func,str):
#     if str == "encode":
#         assert func('abc') == 'fgh', "Test 1 failed"
#         assert func('xyz') == 'cde', "Test 2 failed"
#         assert func('') == '', "Test 3 failed"
#         assert func('hello') == 'mjqqt', "Test 4 failed"

#     else:
#         assert func('fgh') == 'abc', "Test 1 failed"
#         assert func('cde') == 'xyz', "Test 2 failed"
#         assert func('') == '', "Test 3 failed"
#         assert func('mjqqt') == 'hello', "Test 4 failed"

# run_tests(encode_shift_geminicot_pass1,"encode")
# run_tests(encode_shift_geminicot_pass2,"encode")
# run_tests(encode_shift_geminicot_pass3,"encode")
# run_tests(decode_shift_geminicot_pass1,"decode")
# run_tests(decode_shift_geminicot_pass2,"decode")
# run_tests(decode_shift_geminicot_pass3,"decode")

# run_tests(encode_shift_claude_cot_pass1,"encode")
# run_tests(encode_shift_claude_cot_pass2,"encode")
# run_tests(encode_shift_claude_cot_pass3,"encode")
# run_tests(decode_shift_claude_cot_pass1,"decode")
# run_tests(decode_shift_claude_cot_pass2,"decode")
# run_tests(decode_shift_claude_cot_pass3,"decode")


# run_tests(encode_shift_claude_sd_pass1,"encode")
# run_tests(decode_shift_claude_sd_pass1,"decode")
# run_tests(encode_shift_claude_sd_pass2,"encode")
# run_tests(decode_shift_claude_sd_pass2,"decode")
# run_tests(encode_shift_claude_sd_pass3,"encode")
# run_tests(decode_shift_claude_sd_pass3,"decode")

# run_tests(encode_shift_gemini_sd_pass1,"encode")
# run_tests(decode_shift_gemini_sd_pass1,"decode")
# run_tests(encode_shift_gemini_sd_pass2,"encode")
# run_tests(decode_shift_gemini_sd_pass2,"decode")
# run_tests(encode_shift_gemini_sd_pass3,"encode")
# run_tests(decode_shift_gemini_sd_pass3,"decode")

# Restructured to accommodate pytest cov

# test_p10.py
import os, sys, pytest
sys.path.append(os.path.dirname(__file__))

from P10cot_gemini import (
    encode_shift_geminicot_pass1, encode_shift_geminicot_pass2, encode_shift_geminicot_pass3,
    decode_shift_geminicot_pass1, decode_shift_geminicot_pass2, decode_shift_geminicot_pass3,
)
from P10cot_claude import (
    encode_shift_claude_cot_pass1, encode_shift_claude_cot_pass2, encode_shift_claude_cot_pass3,
    decode_shift_claude_cot_pass1, decode_shift_claude_cot_pass2, decode_shift_claude_cot_pass3,
)
from P10sd_claude import (
    encode_shift_claude_sd_pass1, encode_shift_claude_sd_pass2, encode_shift_claude_sd_pass3,
    decode_shift_claude_sd_pass1, decode_shift_claude_sd_pass2, decode_shift_claude_sd_pass3,
)
from P10sd_gemini import (
    encode_shift_gemini_sd_pass1, encode_shift_gemini_sd_pass2, encode_shift_gemini_sd_pass3,
    decode_shift_gemini_sd_pass1, decode_shift_gemini_sd_pass2, decode_shift_gemini_sd_pass3,
)

ENCODE_FUNCS = [
    encode_shift_geminicot_pass1, encode_shift_geminicot_pass2, encode_shift_geminicot_pass3,
    encode_shift_claude_cot_pass1, encode_shift_claude_cot_pass2, encode_shift_claude_cot_pass3,
    encode_shift_claude_sd_pass1,   encode_shift_claude_sd_pass2,   encode_shift_claude_sd_pass3,
    encode_shift_gemini_sd_pass1,   encode_shift_gemini_sd_pass2,   encode_shift_gemini_sd_pass3,
]
ENCODE_IDS = [
    "gemini_cot_e1","gemini_cot_e2","gemini_cot_e3",
    "claude_cot_e1","claude_cot_e2","claude_cot_e3",
    "claude_sd_e1","claude_sd_e2","claude_sd_e3",
    "gemini_sd_e1","gemini_sd_e2","gemini_sd_e3",
]

DECODE_FUNCS = [
    decode_shift_geminicot_pass1, decode_shift_geminicot_pass2, decode_shift_geminicot_pass3,
    decode_shift_claude_cot_pass1, decode_shift_claude_cot_pass2, decode_shift_claude_cot_pass3,
    decode_shift_claude_sd_pass1,   decode_shift_claude_sd_pass2,   decode_shift_claude_sd_pass3,
    decode_shift_gemini_sd_pass1,   decode_shift_gemini_sd_pass2,   decode_shift_gemini_sd_pass3,
]
DECODE_IDS = [
    "gemini_cot_d1","gemini_cot_d2","gemini_cot_d3",
    "claude_cot_d1","claude_cot_d2","claude_cot_d3",
    "claude_sd_d1","claude_sd_d2","claude_sd_d3",
    "gemini_sd_d1","gemini_sd_d2","gemini_sd_d3",
]

ENCODE_CASES = [
    ("abc","fgh"), ("xyz","cde"), ("",""), ("hello","mjqqt"),
]
DECODE_CASES = [
    ("fgh","abc"), ("cde","xyz"), ("",""), ("mjqqt","hello"),
]

@pytest.mark.parametrize("func", ENCODE_FUNCS, ids=ENCODE_IDS)
@pytest.mark.parametrize("inp,expected", ENCODE_CASES)
def test_encode_variants(func, inp, expected):
    assert func(inp) == expected

@pytest.mark.parametrize("func", DECODE_FUNCS, ids=DECODE_IDS)
@pytest.mark.parametrize("inp,expected", DECODE_CASES)
def test_decode_variants(func, inp, expected):
    assert func(inp) == expected