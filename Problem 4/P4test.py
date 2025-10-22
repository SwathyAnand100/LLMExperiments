from P4cot_gemini import gemini_cot_pass1
from P4cot_gemini import gemini_cot_pass2
from P4cot_gemini import gemini_cot_pass3

from P4sd_gemini import gemini_sd_pass1
from P4sd_gemini import gemini_sd_pass2
from P4sd_gemini import gemini_sd_pass3

from P4cot_claude import claude_cot_pass1
from P4cot_claude import claude_cot_pass2
from P4cot_claude import claude_cot_pass3

from P4sd_claude import claude_sd_pass1
from P4sd_claude import claude_sd_pass2
from P4sd_claude import claude_sd_pass3


def run_test(func):
    assert func("Hello WORLd!") == 396, "Test 1 Failed: Standard case sum is incorrect."
    assert func("") == 0, "Test 2 Failed: Empty string should return 0."
    assert func("all lowercase 123") == 0, "Test 3 Failed: String with no uppercase should return 0."
    assert func("ABC") == 198, "Test 4 Failed: Only uppercase letters sum is incorrect."
    assert func("123!@#$XYZ") == 267, "Test 5 Failed: Mixed characters sum is incorrect."
    assert func("Mom") == 77, "Test 6 Failed: Repeated uppercase letters sum is incorrect."

run_test(gemini_cot_pass1)
run_test(gemini_cot_pass2)
run_test(gemini_cot_pass3)

run_test(gemini_sd_pass1)
run_test(gemini_sd_pass2)
run_test(gemini_sd_pass3)

run_test(claude_cot_pass1)
run_test(claude_cot_pass2)
run_test(claude_cot_pass3)

run_test(claude_sd_pass1)
run_test(claude_sd_pass2)
run_test(claude_sd_pass3)