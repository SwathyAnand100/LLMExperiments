# from P9cot_gemini import gemini_cot_pass1
# from P9cot_gemini import gemini_cot_pass2
# from P9cot_gemini import gemini_cot_pass3

# from P9cot_claude import claude_cot_pass1
# from P9cot_claude import claude_cot_pass2
# from P9cot_claude import claude_cot_pass3

# from P9sd_gemini import gemini_sd_pass1
# from P9sd_gemini import gemini_sd_pass2
# from P9sd_gemini import gemini_sd_pass3

# from P9sd_claude import claude_sd_pass1
# from P9sd_claude import claude_sd_pass2
# from P9sd_claude import claude_sd_pass3

# def run_tests(func):
#     print("Running Func ",func)
#     assert func([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11], "Test 1 failed"
#     assert func([]) == [], "Test 2 failed"
#     assert func([101, 12, 45, 67, 89]) == [101, 12, 45, 67, 89], "Test 3 failed"
#     assert func([10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]) == [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19], "Test 4 failed"
#     assert func([23, 2, 9, 34, 8, 9, 10, 74]) == [10, 2, 23, 34, 8, 9, 9, 74], "Test 5 failed"
#     assert func([-101, -12, -45, -67, -89]) == [-101, -12, -45, -67, -89], "Test 6 failed"
#     assert func([0, 100, 200, 300]) == [0, 100, 200, 300], "Test 7 failed"

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

# Restructured to accommodate pytest cov
# test_p9.py
import pytest
import os, sys
sys.path.append(os.path.dirname(__file__))

from P9cot_gemini import gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3
from P9cot_claude import claude_cot_pass1, claude_cot_pass2, claude_cot_pass3
from P9sd_gemini  import gemini_sd_pass1,  gemini_sd_pass2,  gemini_sd_pass3
from P9sd_claude  import claude_sd_pass1,  claude_sd_pass2,  claude_sd_pass3

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

# (input_list, expected_list, id)
CASES = [
    ([1, 11, -1, -11, -12],            [-1, -11, 1, -12, 11], "canonical_example"),
    ([],                               [],                    "empty"),
    ([101, 12, 45, 67, 89],            [101, 12, 45, 67, 89], "already_sorted"),
    ([10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19],
     [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19],           "tie_stable"),
    ([23, 2, 9, 34, 8, 9, 10, 74],     [10, 2, 23, 34, 8, 9, 9, 74], "mixed_digits"),
    ([-101, -12, -45, -67, -89],       [-101, -12, -45, -67, -89],   "all_negative"),
    ([0, 100, 200, 300],               [0, 100, 200, 300],           "zeros_hundreds"),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("arr,expected,_", CASES, ids=[c[2] for c in CASES])
def test_problem9_variants(func, arr, expected, _):
    """Validate custom 'weight' sort logic (stable tie behavior)."""
    assert func(arr) == expected, f"{func.__name__} failed on case '{_}'"
