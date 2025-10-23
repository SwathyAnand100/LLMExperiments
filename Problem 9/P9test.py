from P9cot_gemini import gemini_cot_pass1
from P9cot_gemini import gemini_cot_pass2
from P9cot_gemini import gemini_cot_pass3

from P9cot_claude import claude_cot_pass1
from P9cot_claude import claude_cot_pass2
from P9cot_claude import claude_cot_pass3

from P9sd_gemini import gemini_sd_pass1
from P9sd_gemini import gemini_sd_pass2
from P9sd_gemini import gemini_sd_pass3

from P9sd_claude import claude_sd_pass1
from P9sd_claude import claude_sd_pass2
from P9sd_claude import claude_sd_pass3

def run_tests(func):
    print("Running Func ",func)
    assert func([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11], "Test 1 failed"
    assert func([]) == [], "Test 2 failed"
    assert func([101, 12, 45, 67, 89]) == [101, 12, 45, 67, 89], "Test 3 failed"
    assert func([10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]) == [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19], "Test 4 failed"
    assert func([23, 2, 9, 34, 8, 9, 10, 74]) == [10, 2, 23, 34, 8, 9, 9, 74], "Test 5 failed"
    assert func([-101, -12, -45, -67, -89]) == [-101, -12, -45, -67, -89], "Test 6 failed"
    assert func([0, 100, 200, 300]) == [0, 100, 200, 300], "Test 7 failed"

run_tests(gemini_cot_pass1)
run_tests(gemini_cot_pass2)
run_tests(gemini_cot_pass3)

run_tests(claude_cot_pass1)
run_tests(claude_cot_pass2)
run_tests(claude_cot_pass3)

run_tests(gemini_sd_pass1)
run_tests(gemini_sd_pass2)
run_tests(gemini_sd_pass3)

run_tests(claude_sd_pass1)
run_tests(claude_sd_pass2)
run_tests(claude_sd_pass3)
