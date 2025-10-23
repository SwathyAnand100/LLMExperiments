from P5cot_gemini import gemini_cot_pass1
from P5cot_gemini import gemini_cot_pass2
from P5cot_gemini import gemini_cot_pass3

from P5cot_claude import claude_cot_pass1
from P5cot_claude import claude_cot_pass2
from P5cot_claude import claude_cot_pass3

from P5sd_gemini import gemini_sd_pass1
from P5sd_gemini import gemini_sd_pass2
from P5sd_gemini import gemini_sd_pass3

from P5sd_claude import claude_sd_pass1
from P5sd_claude import claude_sd_pass2
from P5sd_claude import claude_sd_pass3

def run_tests(func):
    print("Running function ",func,":")
    # n < 3: impossible to form a triple
    assert func(1) == 0, "Test 1 failed"
    assert func(2) == 0, "Test 2 failed"
    
    # n=3: C0=1, C1=2. C(1,3)+C(2,3) = 0
    assert func(3) == 0, "Test 3 failed" 
    
    # n=4: C0=1, C1=3. C(3,3) = 1
    assert func(4) == 1, "Test 4 failed" 
    
    # n=5: C0=2, C1=3. C(3,3) = 1
    assert func(5) == 1, "Test 5 failed"
    
    # n=6: C0=2, C1=4. C(4,3) = 4
    assert func(6) == 4, "Test 6 failed"
    
    # n=7: C0=2, C1=5. C(5,3) = 10
    assert func(7) == 10, "Test 7 failed"
    
    # n=8: C0=3, C1=5. C(3,3)+C(5,3) = 1+10 = 11
    assert func(8) == 11, "Test 8 failed"
    
    # n=9: C0=3, C1=6. C(3,3)+C(6,3) = 1+20 = 21
    assert func(9) == 21, "Test 9 failed"
    
    # n=10: C0=3, C1=7. C(3,3)+C(7,3) = 1+35 = 36
    assert func(10) == 36, "Test 10 failed"



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