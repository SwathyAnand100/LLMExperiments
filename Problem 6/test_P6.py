# from P6cot_gemini import gemini_cot_pass1
# from P6cot_gemini import gemini_cot_pass2
# from P6cot_gemini import gemini_cot_pass3

# from P6cot_claude import claude_cot_pass1
# from P6cot_claude import claude_cot_pass2
# from P6cot_claude import claude_cot_pass3

# from P6sd_gemini import gemini_sd_pass1
# from P6sd_gemini import gemini_sd_pass2
# from P6sd_gemini import gemini_sd_pass3

# from P6sd_claude import claude_sd_pass1
# from P6sd_claude import claude_sd_pass2
# from P6sd_claude import claude_sd_pass3

# def run_tests(func):
#     print("Running Function ", func)
#     assert func("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Test 1 failed"
#     assert func("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "Test 2 failed"
#     assert func("") == [], "Test 3 failed"
#     assert func("apple,banana,carrot") == ["apple", "banana", "carrot"], "Test 4 failed"
#     assert func("apple banana carrot") == ["apple", "banana", "carrot"], "Test 5 failed"
#     assert func("apple, banana,carrot") == ["apple", "banana", "carrot"], "Test 6 failed"
#     assert func("apple , banana , carrot") == ["apple", "banana", "carrot"], "Test 7 failed"
#     assert func("apple, ,banana, ,carrot") == ["apple", "banana", "carrot"], "Test 8 failed"
#     assert func(" , , , ") == [], "Test 9 failed"

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
# test_p6.py

# test_p6.py
import pytest
import os, sys
sys.path.append(os.path.dirname(__file__))

from P6cot_gemini import gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3
from P6cot_claude import claude_cot_pass1, claude_cot_pass2, claude_cot_pass3
from P6sd_gemini import gemini_sd_pass1, gemini_sd_pass2, gemini_sd_pass3
from P6sd_claude import claude_sd_pass1, claude_sd_pass2, claude_sd_pass3

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

# (input_string, expected_list, id)
CASES = [
    ("Hi, my name is John", ["Hi","my","name","is","John"], "standard"),
    ("One, two, three, four, five, six",
     ["One","two","three","four","five","six"], "comma_spaced"),
    ("", [], "empty"),
    ("apple,banana,carrot", ["apple","banana","carrot"], "comma_no_space"),
    ("apple banana carrot", ["apple","banana","carrot"], "space_only"),
    ("apple, banana,carrot", ["apple","banana","carrot"], "mixed_spacing"),
    ("apple , banana , carrot", ["apple","banana","carrot"], "extra_spaces"),
    ("apple, ,banana, ,carrot", ["apple","banana","carrot"], "double_commas"),
    (" , , , ", [], "only_commas"),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("s,expected,_", CASES, ids=[c[2] for c in CASES])
def test_problem6_variants(func, s, expected, _):
    """Verify token splitting logic for different delimiter patterns."""
    result = func(s)
    assert result == expected, f"{func.__name__} failed on case '{_}'"
