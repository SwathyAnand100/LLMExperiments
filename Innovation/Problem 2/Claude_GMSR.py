#PROMPT:
# Create a Python function that checks if the last character of a given string is a letter (a–z or A–Z). 
# The function should return True if it is a letter, otherwise False.
# Examples:
# "Abc" -> True
# "abc!" -> False
# ""  -> False
# Agents and Roles:
# Planner - Explain how to handle different cases (empty strings, special characters, whitespace). Outline the logic clearly.
# Solver - Implement the function in clean, efficient Python code with inline comments explaining each step.
# Verifier - Design and run test cases including edge cases like empty strings, symbols, numbers, and mixed characters. Report any failures or inconsistencies.
# Refiner - Improve based on verifier feedback, ensuring robust handling of Unicode and whitespace, and produce the final clean implementation with a brief explanation.
# Goal:
# Deliver a function that is logically sound, handles all edge cases, and passes all verification tests.
"""
Three different implementations to check if the last character 
of a string is a letter (a-z or A-Z).
"""


# ============================================================
# IMPLEMENTATION 1: Using .isalpha() and .isascii()
# ============================================================
# Most Pythonic and readable approach
def is_last_char_letter_v1(s):
    """
    Check using built-in string methods.
    
    Pros: Most readable, concise, Pythonic
    Cons: Two method calls
    """
    if not s:
        return False
    return s[-1].isalpha() and s[-1].isascii()


# ============================================================
# IMPLEMENTATION 2: Using ASCII code ranges
# ============================================================
# Manual character code checking for maximum control
def is_last_char_letter_v2(s):
    """
    Check using ASCII code ranges.
    
    Pros: No method calls, explicit logic, potentially faster
    Cons: Less readable, manual range checking
    """
    if not s:
        return False
    
    # Get ASCII code of last character
    char_code = ord(s[-1])
    
    # Check if in ranges: A-Z (65-90) or a-z (97-122)
    return (65 <= char_code <= 90) or (97 <= char_code <= 122)


# ============================================================
# IMPLEMENTATION 3: Using regular expressions
# ============================================================
# Pattern matching approach
import re

def is_last_char_letter_v3(s):
    """
    Check using regex pattern matching.
    
    Pros: Powerful for complex patterns, one-liner logic
    Cons: Regex overhead, slight performance cost for simple check
    """
    if not s:
        return False
    
    # Match only if last character is a-z or A-Z
    return bool(re.match(r'^[a-zA-Z]$', s[-1]))


# ============================================================
# TEST ALL IMPLEMENTATIONS
# ============================================================
def test_all_implementations():
    """Run comprehensive tests on all three implementations."""
    
    implementations = [
        ("Version 1 (isalpha + isascii)", is_last_char_letter_v1),
        ("Version 2 (ASCII codes)", is_last_char_letter_v2),
        ("Version 3 (Regex)", is_last_char_letter_v3),
    ]
    
    test_cases = [
        ("Abc", True),
        ("abc!", False),
        ("", False),
        ("hello ", False),
        ("test123", False),
        ("xyz", True),
        ("XYZ", True),
        ("test@", False),
        ("a", True),
        ("1", False),
        ("!", False),
        ("123abc", True),
        ("abc123", False),
        ("hello\n", False),
    ]
    
    print("=" * 70)
    print("TESTING ALL THREE IMPLEMENTATIONS")
    print("=" * 70)
    
    for impl_name, impl_func in implementations:
        print(f"\n{impl_name}:")
        print("-" * 70)
        
        passed = 0
        failed = 0
        
        for input_str, expected in test_cases:
            result = impl_func(input_str)
            status = "✓" if result == expected else "✗"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            # Show representation for special chars
            display = repr(input_str) if any(c in input_str for c in ['\n', '\t', ' ']) or not input_str else f"'{input_str}'"
            print(f"  {status} {display:20s} -> {result:5} (expected {expected})")
        
        print(f"\n  Result: {passed}/{len(test_cases)} passed")
        
        if failed > 0:
            print(f"  ⚠️  {failed} test(s) failed!")
    
    print("\n" + "=" * 70)
    print("RECOMMENDATION:")
    print("=" * 70)
    print("✓ Use Version 1 for most cases (best readability)")
    print("✓ Use Version 2 if performance is critical")
    print("✓ Use Version 3 if you're already using regex elsewhere")


# Run the tests
if __name__ == "__main__":
    test_all_implementations()