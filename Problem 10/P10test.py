from P10cot_gemini import encode_shift_geminicot_pass1
from P10cot_gemini import encode_shift_geminicot_pass2
from P10cot_gemini import encode_shift_geminicot_pass3
from P10cot_gemini import decode_shift_geminicot_pass1
from P10cot_gemini import decode_shift_geminicot_pass2
from P10cot_gemini import decode_shift_geminicot_pass3

from P10cot_claude import encode_shift_claude_cot_pass1
from P10cot_claude import encode_shift_claude_cot_pass2
from P10cot_claude import encode_shift_claude_cot_pass3
from P10cot_claude import decode_shift_claude_cot_pass1
from P10cot_claude import decode_shift_claude_cot_pass2
from P10cot_claude import decode_shift_claude_cot_pass3

from P10sd_claude import encode_shift_claude_sd_pass1
from P10sd_claude import encode_shift_claude_sd_pass2
from P10sd_claude import encode_shift_claude_sd_pass3
from P10sd_claude import decode_shift_claude_sd_pass1
from P10sd_claude import decode_shift_claude_sd_pass2
from P10sd_claude import decode_shift_claude_sd_pass3

from P10sd_gemini import encode_shift_gemini_sd_pass1
from P10sd_gemini import encode_shift_gemini_sd_pass2
from P10sd_gemini import encode_shift_gemini_sd_pass3
from P10sd_gemini import decode_shift_gemini_sd_pass1
from P10sd_gemini import decode_shift_gemini_sd_pass2
from P10sd_gemini import decode_shift_gemini_sd_pass3

def run_tests(func,str):
    if str == "encode":
        assert func('abc') == 'fgh', "Test 1 failed"
        assert func('xyz') == 'cde', "Test 2 failed"
        assert func('') == '', "Test 3 failed"
        assert func('hello') == 'mjqqt', "Test 4 failed"

    else:
        assert func('fgh') == 'abc', "Test 1 failed"
        assert func('cde') == 'xyz', "Test 2 failed"
        assert func('') == '', "Test 3 failed"
        assert func('mjqqt') == 'hello', "Test 4 failed"

run_tests(encode_shift_geminicot_pass1,"encode")
run_tests(encode_shift_geminicot_pass2,"encode")
run_tests(encode_shift_geminicot_pass3,"encode")
run_tests(decode_shift_geminicot_pass1,"decode")
run_tests(decode_shift_geminicot_pass2,"decode")
run_tests(decode_shift_geminicot_pass3,"decode")

run_tests(encode_shift_claude_cot_pass1,"encode")
run_tests(encode_shift_claude_cot_pass2,"encode")
run_tests(encode_shift_claude_cot_pass3,"encode")
run_tests(decode_shift_claude_cot_pass1,"decode")
run_tests(decode_shift_claude_cot_pass2,"decode")
run_tests(decode_shift_claude_cot_pass3,"decode")


run_tests(encode_shift_claude_sd_pass1,"encode")
run_tests(decode_shift_claude_sd_pass1,"decode")
run_tests(encode_shift_claude_sd_pass2,"encode")
run_tests(decode_shift_claude_sd_pass2,"decode")
run_tests(encode_shift_claude_sd_pass3,"encode")
run_tests(decode_shift_claude_sd_pass3,"decode")

run_tests(encode_shift_gemini_sd_pass1,"encode")
run_tests(decode_shift_gemini_sd_pass1,"decode")
run_tests(encode_shift_gemini_sd_pass2,"encode")
run_tests(decode_shift_gemini_sd_pass2,"decode")
run_tests(encode_shift_gemini_sd_pass3,"encode")
run_tests(decode_shift_gemini_sd_pass3,"decode")