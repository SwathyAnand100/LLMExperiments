from P3cot_gemini import gemini_cot_pass1
from P3cot_gemini import gemini_cot_pass2
from P3cot_gemini import gemini_cot_pass3

from P3cot_claude import claude_cot_pass1
from P3cot_claude import claude_cot_pass2
from P3cot_claude import claude_cot_pass3

from P3sd_gemini import gemini_sd_pass1
from P3sd_gemini import gemini_sd_pass2
from P3sd_gemini import gemini_sd_pass3

from P3sd_claude import claude_sd_pass1
from P3sd_claude import claude_sd_pass2
from P3sd_claude import claude_sd_pass3

def run_test(func):
    assert func("Hello World!") == "Hll Wrld!", "Test Case 1 Failed: Standard string"
    assert func("AEIOUaeiou") == "", "Test Case 2 Failed: All vowels"
    assert func("rhythm") == "rhythm", "Test Case 3 Failed: No vowels"
    assert func("") == "", "Test Case 4 Failed: Empty string"
    assert func("Test 123.\nNew Line!") == "Tst 123.\nNw Ln!", "Test Case 5 Failed: Mixed characters"
    assert func("example sentence") == "xmpl sntnc", "Test Case 6 Failed: Lowercase only"
    assert func("EDUCATION") == "DCTN", "Test Case 7 Failed: Uppercase only"
    assert func("a") == "", "Test Case 8a Failed: Single vowel"
    assert func("b") == "b", "Test Case 8b Failed: Single consonant"
    assert func("7") == "7", "Test Case 8c Failed: Single number"


run_test(gemini_cot_pass1)
run_test(gemini_cot_pass2)
run_test(gemini_cot_pass3)

run_test(claude_cot_pass1)
run_test(claude_cot_pass2)
run_test(claude_cot_pass3)

run_test(gemini_sd_pass1)
run_test(gemini_sd_pass2)
run_test(gemini_sd_pass3)

run_test(claude_sd_pass1)
run_test(claude_sd_pass2)
run_test(claude_sd_pass3)