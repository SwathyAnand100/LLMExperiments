# from P3cot_gemini import gemini_cot_pass1
# from P3cot_gemini import gemini_cot_pass2
# from P3cot_gemini import gemini_cot_pass3

# from P3cot_claude import claude_cot_pass1
# from P3cot_claude import claude_cot_pass2
# from P3cot_claude import claude_cot_pass3

# from P3sd_gemini import gemini_sd_pass1
# from P3sd_gemini import gemini_sd_pass2
# from P3sd_gemini import gemini_sd_pass3

# from P3sd_claude import claude_sd_pass1
# from P3sd_claude import claude_sd_pass2
# from P3sd_claude import claude_sd_pass3

# def run_test(func):
#     assert func("Hello World!") == "Hll Wrld!", "Test Case 1 Failed: Standard string"
#     assert func("AEIOUaeiou") == "", "Test Case 2 Failed: All vowels"
#     assert func("rhythm") == "rhythm", "Test Case 3 Failed: No vowels"
#     assert func("") == "", "Test Case 4 Failed: Empty string"
#     assert func("Test 123.\nNew Line!") == "Tst 123.\nNw Ln!", "Test Case 5 Failed: Mixed characters"
#     assert func("example sentence") == "xmpl sntnc", "Test Case 6 Failed: Lowercase only"
#     assert func("EDUCATION") == "DCTN", "Test Case 7 Failed: Uppercase only"
#     assert func("a") == "", "Test Case 8a Failed: Single vowel"
#     assert func("b") == "b", "Test Case 8b Failed: Single consonant"
#     assert func("7") == "7", "Test Case 8c Failed: Single number"


# run_test(gemini_cot_pass1)
# run_test(gemini_cot_pass2)
# run_test(gemini_cot_pass3)

# run_test(claude_cot_pass1)
# run_test(claude_cot_pass2)
# run_test(claude_cot_pass3)

# run_test(gemini_sd_pass1)
# run_test(gemini_sd_pass2)
# run_test(gemini_sd_pass3)

# run_test(claude_sd_pass1)
# run_test(claude_sd_pass2)
# run_test(claude_sd_pass3)

#Restructuing tests for better readability for pytest.cov
# test_p3.py
import pytest
import os, sys

# ensure local imports work
sys.path.append(os.path.dirname(__file__))

from P3cot_gemini import gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3
from P3cot_claude import claude_cot_pass1, claude_cot_pass2, claude_cot_pass3
from P3sd_gemini import gemini_sd_pass1, gemini_sd_pass2, gemini_sd_pass3
from P3sd_claude import claude_sd_pass1, claude_sd_pass2, claude_sd_pass3

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

# (input_string, expected_output, id)
CASES = [
    ("Hello World!",        "Hll Wrld!",    "standard"),
    ("AEIOUaeiou",          "",             "all_vowels"),
    ("rhythm",              "rhythm",       "no_vowels"),
    ("",                    "",             "empty"),
    ("Test 123.\nNew Line!","Tst 123.\nNw Ln!", "mixed_chars"),
    ("example sentence",    "xmpl sntnc",   "lowercase_only"),
    ("EDUCATION",           "DCTN",         "uppercase_only"),
    ("a",                   "",             "single_vowel"),
    ("b",                   "b",            "single_consonant"),
    ("7",                   "7",            "single_number"),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("inp,expected,_", CASES, ids=[c[2] for c in CASES])
def test_problem3_variants(func, inp, expected, _):
    """Verify each variant correctly removes vowels."""
    result = func(inp)
    assert result == expected, f"{func.__name__} failed on case '{_}'"
