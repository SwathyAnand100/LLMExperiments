from problem_2 import gemini_cot_pass1
from problem_2 import gemini_cot_pass2
from problem_2 import gemini_cot_pass3

from problem_2 import gemini_sd_pass1
from problem_2 import gemini_sd_pass2
from problem_2 import gemini_sd_pass3

from problem_2 import claude_cot_pass1
from problem_2 import claude_cot_pass2
from problem_2 import claude_cot_pass3

from problem_2 import claude_sd_pass1 
from problem_2 import claude_sd_pass2
from problem_2 import claude_sd_pass3

def run_test(func):
    assert func("Hello world a") == True, "Test Case 1 Failed: Alphabetical, preceded by space"
    assert func("end of line B") == True, "Test Case 2 Failed: Alphabetical, preceded by space, uppercase"

    # Case 2: Alphabetical and single character
    assert func("a") == True, "Test Case 3 Failed: Alphabetical, single character"
    assert func("Z") == True, "Test Case 4 Failed: Alphabetical, single character, uppercase"
    assert func(" hello w") == True, "Test Case 5 Failed: Alphabetical, preceded by space after leading space"

    # Case 3: Last character is NOT alphabetical
    assert func("Hello world!") == False, "Test Case 6 Failed: Last char is not alphabetical ('!')"
    assert func("String 5") == False, "Test Case 7 Failed: Last char is not alphabetical ('5')"
    assert func("test space ") == False, "Test Case 8 Failed: Last char is a space"
    assert func("") == False, "Test Case 9 Failed: Empty string"
    assert func(" ") == False, "Test Case 10 Failed: Single space string"

    # Case 4: Last character IS alphabetical but IS part of a word (preceded by non-space)
    assert func("Test stringZ") == False, "Test Case 11 Failed: Alphabetical, part of word"
    assert func("another word") == False, "Test Case 12 Failed: Alphabetical, part of word"


run_test(gemini_cot_pass1)
run_test(gemini_cot_pass2)
run_test(gemini_cot_pass3)

run_test(gemini_sd_pass1)
run_test(gemini_sd_pass2)
run_test(gemini_sd_pass3)

run_test(claude_sd_pass1)
run_test(claude_sd_pass2)
run_test(claude_sd_pass3)

run_test(claude_cot_pass1)
run_test(claude_cot_pass2)
run_test(claude_cot_pass3)