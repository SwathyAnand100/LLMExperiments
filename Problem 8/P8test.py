from P8cot_gemini import gemini_cot_pass1
from P8cot_gemini import gemini_cot_pass2
from P8cot_gemini import gemini_cot_pass3

from P8cot_claude import claude_cot_pass1
from P8cot_claude import claude_cot_pass2
from P8cot_claude import claude_cot_pass3

from P8sd_gemini import gemini_sd_pass1
from P8sd_gemini import gemini_sd_pass2
from P8sd_gemini import gemini_sd_pass3

from P8sd_claude import claude_sd_pass1
from P8sd_claude import claude_sd_pass2
from P8sd_claude import claude_sd_pass3

def run_tests(func):
    print("Running Function ",func)
    assert func("Hello world!") == ["Hello", "world!"], "Test 1 failed"
    assert func("Hello,world!") == ["Hello", "world!"], "Test 2 failed"
    assert func("abcdef") == 3, "Test 3 failed"
    assert func("a,c,e") == ["a", "c", "e"], "Test 4 failed"
    assert func("a b c") == ["a", "b", "c"], "Test 5 failed"
    assert func("xyz") == 2, "Test 6 failed"  # Only 'x' (23), 'y' (24), 'z' (25); 'x' and 'z' are odd positions
    assert func("") == 0, "Test 7 failed"
    assert func("A,B,C") == ["A", "B", "C"], "Test 8 failed"
    assert func("A B C") == ["A", "B", "C"], "Test 9 failed"
    assert func("acegik") == 0, "Test 10 failed"


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


