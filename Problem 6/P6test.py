from P6cot_gemini import gemini_cot_pass1
from P6cot_gemini import gemini_cot_pass2
from P6cot_gemini import gemini_cot_pass3

from P6cot_claude import claude_cot_pass1
from P6cot_claude import claude_cot_pass2
from P6cot_claude import claude_cot_pass3

from P6sd_gemini import gemini_sd_pass1
from P6sd_gemini import gemini_sd_pass2
from P6sd_gemini import gemini_sd_pass3

from P6sd_claude import claude_sd_pass1
from P6sd_claude import claude_sd_pass2
from P6sd_claude import claude_sd_pass3

def run_tests(func):
    print("Running Function ", func)
    assert func("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Test 1 failed"
    assert func("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "Test 2 failed"
    assert func("") == [], "Test 3 failed"
    assert func("apple,banana,carrot") == ["apple", "banana", "carrot"], "Test 4 failed"
    assert func("apple banana carrot") == ["apple", "banana", "carrot"], "Test 5 failed"
    assert func("apple, banana,carrot") == ["apple", "banana", "carrot"], "Test 6 failed"
    assert func("apple , banana , carrot") == ["apple", "banana", "carrot"], "Test 7 failed"
    assert func("apple, ,banana, ,carrot") == ["apple", "banana", "carrot"], "Test 8 failed"
    assert func(" , , , ") == [], "Test 9 failed"

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


