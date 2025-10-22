from problem_1 import gemini_cot_pass1
from problem_1 import gemini_cot_pass2
from problem_1 import gemini_cot_pass3

from problem_1 import gemini_sd_pass1
from problem_1 import gemini_sd_pass2
from problem_1 import gemini_sd_pass3

from problem_1 import claude_cot_pass1
from problem_1 import claude_cot_pass2
from problem_1 import claude_cot_pass3

from problem_1 import claude_sd_pass1
from problem_1 import claude_sd_pass2
from problem_1 import claude_sd_pass3

def run_tests(func):
    assert func([1,2,3,4,5],10),"Test 1 failed."
    assert not func([1,2,9,4,5],8),"Test 2 failed."
    assert not func([10,20,30],30),"Test 3 failed."
    assert not func([5,5,5],5),"Test 4 failed."
    assert func([],5),"Test 5 failed."
    assert func([-10,0,15,-200],16),"Test 6 failed."
    assert func([1.5,2.3],3.0),"Test 7 failed."


run_tests(gemini_cot_pass1)
run_tests(gemini_cot_pass2)
run_tests(gemini_cot_pass3)

run_tests(gemini_sd_pass1)
run_tests(gemini_sd_pass2)
run_tests(gemini_sd_pass3)

run_tests(claude_cot_pass1)
run_tests(claude_cot_pass2)
run_tests(claude_cot_pass3)

run_tests(claude_sd_pass1)
run_tests(claude_sd_pass2)
run_tests(claude_sd_pass3)