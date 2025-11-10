# from P8cot_gemini import gemini_cot_pass1
# from P8cot_gemini import gemini_cot_pass2
# from P8cot_gemini import gemini_cot_pass3

# from P8cot_claude import claude_cot_pass1
# from P8cot_claude import claude_cot_pass2
# from P8cot_claude import claude_cot_pass3

# from P8sd_gemini import gemini_sd_pass1
# from P8sd_gemini import gemini_sd_pass2
# from P8sd_gemini import gemini_sd_pass3

# from P8sd_claude import claude_sd_pass1
# from P8sd_claude import claude_sd_pass2
# from P8sd_claude import claude_sd_pass3

# def run_tests(func):
#     print("Running Function ",func)
#     assert func("Hello world!") == ["Hello", "world!"], "Test 1 failed"
#     assert func("Hello,world!") == ["Hello", "world!"], "Test 2 failed"
#     assert func("abcdef") == 3, "Test 3 failed"
#     assert func("a,c,e") == ["a", "c", "e"], "Test 4 failed"
#     assert func("a b c") == ["a", "b", "c"], "Test 5 failed"
#     assert func("xyz") == 2, "Test 6 failed"  # Only 'x' (23), 'y' (24), 'z' (25); 'x' and 'z' are odd positions
#     assert func("") == 0, "Test 7 failed"
#     assert func("A,B,C") == ["A", "B", "C"], "Test 8 failed"
#     assert func("A B C") == ["A", "B", "C"], "Test 9 failed"
#     assert func("acegik") == 0, "Test 10 failed"


# run_tests(gemini_cot_pass1)
# run_tests(gemini_cot_pass2)
# run_tests(gemini_cot_pass3)

# run_tests(claude_cot_pass1)
# run_tests(claude_cot_pass2)
# run_tests(claude_cot_pass3)


# run_tests(gemini_sd_pass1)
# run_tests(gemini_sd_pass2)
# run_tests(gemini_sd_pass3)

# run_tests(claude_sd_pass1)
# run_tests(claude_sd_pass2)
# run_tests(claude_sd_pass3)


#Restructuing tests for better readability for pytest.cov
# test_p8.py
# test_p8.py
import pytest
import os, sys
sys.path.append(os.path.dirname(__file__))

from P8cot_gemini import gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3
from P8cot_claude import claude_cot_pass1, claude_cot_pass2, claude_cot_pass3
from P8sd_gemini  import gemini_sd_pass1,  gemini_sd_pass2,  gemini_sd_pass3
from P8sd_claude  import claude_sd_pass1,  claude_sd_pass2,  claude_sd_pass3

FUNCS = [
    gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3,
    claude_cot_pass1, claude_cot_pass2, claude_cot_pass3,
    gemini_sd_pass1,  gemini_sd_pass2,  gemini_sd_pass3,
    claude_sd_pass1,  claude_sd_pass2,  claude_sd_pass3,
]
FUNC_IDS = [
    "gemini_cot_pass1","gemini_cot_pass2","gemini_cot_pass3",
    "claude_cot_pass1","claude_cot_pass2","claude_cot_pass3",
    "gemini_sd_pass1","gemini_sd_pass2","gemini_sd_pass3",
    "claude_sd_pass1","claude_sd_pass2","claude_sd_pass3",
]

# Each case is (input_string, expected_output, id)
# Expected outputs mix list-of-words and integer counts — that matches your spec.
CASES = [
    ("Hello world!",        ["Hello","world!"], "space_split"),
    ("Hello,world!",        ["Hello","world!"], "comma_split"),
    ("abcdef",              3,                  "odd-index-lowercase-count"),
    ("a,c,e",               ["a","c","e"],      "comma_split_multi"),
    ("a b c",               ["a","b","c"],      "space_split_multi"),
    ("xyz",                 2,                  "odd-index-count_xyz"),
    ("",                    0,                  "empty_string"),
    ("A,B,C",               ["A","B","C"],      "comma_split_caps"),
    ("A B C",               ["A","B","C"],      "space_split_caps"),
    ("acegik",              0,                  "no_odd_positions"),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("s,expected,_", CASES, ids=[c[2] for c in CASES])
def test_problem8_variants(func, s, expected, _):
    assert func(s) == expected, f"{func.__name__} failed on case '{_}'"
