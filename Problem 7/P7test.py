from P7cot_gemini import gemini_cot_pass1
from P7cot_gemini import gemini_cot_pass2
from P7cot_gemini import gemini_cot_pass3

from P7cot_claude import claude_cot_pass1
from P7cot_claude import claude_cot_pass2
from P7cot_claude import claude_cot_pass3

from P7sd_gemini import gemini_sd_pass1
from P7sd_gemini import gemini_sd_pass2
from P7sd_gemini import gemini_sd_pass3

from P7sd_claude import claude_sd_pass1
from P7sd_claude import claude_sd_pass2
from P7sd_claude import claude_sd_pass3

def run_tests(func):
    assert func(15) == 5, "Test 1 failed"
    assert func(10) == 5, "Test 2 failed"
    assert func(9) == 3, "Test 3 failed"
    assert func(8) == 4, "Test 4 failed"
    assert func(7) == 1, "Test 5 failed"
    assert func(6) == 3, "Test 6 failed"
    assert func(5) == 1, "Test 7 failed"
    assert func(4) == 2, "Test 8 failed"
    assert func(3) == 1, "Test 9 failed"
    assert func(2) == 1, "Test 10 failed"

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


