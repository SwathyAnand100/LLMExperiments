# from problem_1 import gemini_cot_pass1
# from problem_1 import gemini_cot_pass2
# from problem_1 import gemini_cot_pass3

# from problem_1 import gemini_sd_pass1
# from problem_1 import gemini_sd_pass2
# from problem_1 import gemini_sd_pass3

# from problem_1 import claude_cot_pass1
# from problem_1 import claude_cot_pass2
# from problem_1 import claude_cot_pass3

# from problem_1 import claude_sd_pass1
# from problem_1 import claude_sd_pass2
# from problem_1 import claude_sd_pass3

# def run_tests(func):
#     assert func([1,2,3,4,5],10),"Test 1 failed."
#     assert not func([1,2,9,4,5],8),"Test 2 failed."
#     assert not func([10,20,30],30),"Test 3 failed."
#     assert not func([5,5,5],5),"Test 4 failed."
#     assert func([],5),"Test 5 failed."
#     assert func([-10,0,15,-200],16),"Test 6 failed."
#     assert func([1.5,2.3],3.0),"Test 7 failed."


# run_tests(gemini_cot_pass1)
# run_tests(gemini_cot_pass2)
# run_tests(gemini_cot_pass3)

# run_tests(gemini_sd_pass1)
# run_tests(gemini_sd_pass2)
# run_tests(gemini_sd_pass3)

# run_tests(claude_cot_pass1)
# run_tests(claude_cot_pass2)
# run_tests(claude_cot_pass3)

# run_tests(claude_sd_pass1)
# run_tests(claude_sd_pass2)
# run_tests(claude_sd_pass3)

#Restructuing tests for better readability for pytest.cov
# test_p1.py
import pytest

from problem_1 import (
    gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3,
    gemini_sd_pass1,  gemini_sd_pass2,  gemini_sd_pass3,
    claude_cot_pass1, claude_cot_pass2, claude_cot_pass3,
    claude_sd_pass1,  claude_sd_pass2,  claude_sd_pass3,
)

FUNCS = [
    gemini_cot_pass1, gemini_cot_pass2, gemini_cot_pass3,
    gemini_sd_pass1,  gemini_sd_pass2,  gemini_sd_pass3,
    claude_cot_pass1, claude_cot_pass2, claude_cot_pass3,
    claude_sd_pass1,  claude_sd_pass2,  claude_sd_pass3,
]

FUNC_IDS = [
    "gemini_cot_pass1","gemini_cot_pass2","gemini_cot_pass3",
    "gemini_sd_pass1","gemini_sd_pass2","gemini_sd_pass3",
    "claude_cot_pass1","claude_cot_pass2","claude_cot_pass3",
    "claude_sd_pass1","claude_sd_pass2","claude_sd_pass3",
]

# Test cases derived from your original assertions:
# (arr, target, expected_bool)
CASES = [
    ([1,2,3,4,5],      10, True),   # was: assert func(...,10)
    ([1,2,9,4,5],       8, False),  # was: assert not func(...,8)
    ([10,20,30],       30, False),
    ([5,5,5],           5, False),
    ([],                5, True),
    ([-10,0,15,-200],  16, True),
    ([1.5,2.3],         3.0, True),
]

@pytest.mark.parametrize("func", FUNCS, ids=FUNC_IDS)
@pytest.mark.parametrize("arr,target,expected", CASES, ids=[
    "sum10","no8","no30","no5","empty5","negatives16","floats3"
])
def test_problem1_variants(func, arr, target, expected):
    result = func(arr, target)
    assert bool(result) is expected


# To run the tests, use the command:
#python -m pytest -p pytest_cov --cov=. --cov-branch --cov-report=term-missing
