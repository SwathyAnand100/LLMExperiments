# from P7cot_gemini import gemini_cot_pass1
# from P7cot_gemini import gemini_cot_pass2
# from P7cot_gemini import gemini_cot_pass3

# from P7cot_claude import claude_cot_pass1
# from P7cot_claude import claude_cot_pass2
# from P7cot_claude import claude_cot_pass3

# from P7sd_gemini import gemini_sd_pass1
# from P7sd_gemini import gemini_sd_pass2
# from P7sd_gemini import gemini_sd_pass3

# from P7sd_claude import claude_sd_pass1
# from P7sd_claude import claude_sd_pass2
# from P7sd_claude import claude_sd_pass3

# def run_tests(func):
#     assert func(15) == 5, "Test 1 failed"
#     assert func(10) == 5, "Test 2 failed"
#     assert func(9) == 3, "Test 3 failed"
#     assert func(8) == 4, "Test 4 failed"
#     assert func(7) == 1, "Test 5 failed"
#     assert func(6) == 3, "Test 6 failed"
#     assert func(5) == 1, "Test 7 failed"
#     assert func(4) == 2, "Test 8 failed"
#     assert func(3) == 1, "Test 9 failed"
#     assert func(2) == 1, "Test 10 failed"

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

# test_p7.py
import pytest
import os, sys

# Ensure local imports work
sys.path.append(os.path.dirname(__file__))

from P7cot_gemini import gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3
from P7cot_claude import claude_cot_pass1, claude_cot_pass2, claude_cot_pass3
from P7sd_gemini import gemini_sd_pass1, gemini_sd_pass2, gemini_sd_pass3
from P7sd_claude import claude_sd_pass1, claude_sd_pass2, claude_sd_pass3

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

# (input_n, expected_output, description)
CASES = [
    (15, 5, "n=15"),
    (10, 5, "n=10"),
    (9,  3, "n=9"),
    (8,  4, "n=8"),
    (7,  1, "n=7"),
    (6,  3, "n=6"),
    (5,  1, "n=5"),
    (4,  2, "n=4"),
    (3,  1, "n=3"),
    (2,  1, "n=2"),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("n,expected,_", CASES, ids=[c[2] for c in CASES])
def test_problem7_variants(func, n, expected, _):
    """Verify integer-processing logic for various input values."""
    result = func(n)
    assert result == expected, f"{func.__name__} failed on case '{_}'"
