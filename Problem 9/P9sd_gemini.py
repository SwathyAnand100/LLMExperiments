# Write a function that sorts a list of integers.
# Crucially, the provided example reveals a non-standard sorting key calculation.
# Input: [1, 11, -1, -11, -12] Required Output: [-1, -11, 1, -12, 11]
# Step 1: Determine the Sorting Key (Weight) and Tie-breaker Rule.
# Analyze the input and required output to deduce the exact "weight" calculation for each number.
# Example: For the input numbers, we must find a set of keys (weights) that, when sorted, results in the required output:
# 1 (Weight: 1)
# 11 (Weight: 2)
#  −1 (Weight: −1)
# −11 (Weight: 0)
# −12 (Weight: 1)
# The sorted order of weights is: −1,0,1,1,2. This corresponds to the output: [−1,−11,1,−12,11].
# State the precise rule for calculating the weight, especially how negative numbers are handled.
# Rule: The weight is the sum of the digits, where the negative sign (if present) is applied only to the first (most significant) digit.
# Example: Weight(−12) = −1+2=1.
# Example: Weight(12) = 1+2=3.
# State the rule for resolving ties (e.g., stable sort or a secondary key).
# Tie-breaker: The numbers 1 and −12 both have a weight of 1. Since 1 appears before −12 in the input, they must appear in the same order in the output. The sort is stable.
# Step 2: Implement the Key Calculation Function.
# Create a helper function weight(x) that implements the rule deduced in Step 1.
# Use string manipulation to easily separate the sign and the digits.
# Step 3: Implement the Final Sorting Function.
# Use the sorted() function with the weight function as the key to ensure the final sorted list meets the requirements (ascending by weight, stable for ties).
# After implementing, check your function against the example [1, 11, -1, -11, -12] => [-1, -11, 1, -12, 11]. 
# If your output differs, debug your key function and sorting approach, explaining any fixes you make. Explain the rationale.
# --- Implementation 1: Pure String Manipulation (Most Readable) ---
def gemini_sd_pass1(nums: list[int]) -> list[int]:
    """Sorts based on non-standard weight: sign only applies to the first digit."""
    
    def weight(x: int) -> int:
        s = str(x)
        total_weight = 0
        
        if s.startswith('-'):
            # The first digit after the sign (s[1]) is negated.
            total_weight -= int(s[1])
            # The remaining digits (s[2:]) are added positively.
            for digit_char in s[2:]:
                total_weight += int(digit_char)
        else:
            # All digits are added positively.
            for digit_char in s:
                total_weight += int(digit_char)
                
        return total_weight

    return sorted(nums, key=weight)

# --- Implementation 2: Hybrid String/List Comprehension (Concise) ---
def gemini_sd_pass2(nums: list[int]) -> list[int]:
    """Sorts using a concise list comprehension and ternary logic for weight."""
    
    def weight(x: int) -> int:
        s = str(x)
        if s.startswith('-'):
            # Create a list where the first digit is negated, and the rest are positive.
            # Example: '-12' -> [-1, 2]
            digit_list = [-int(s[1])] + [int(d) for d in s[2:]]
        else:
            # All digits are positive.
            digit_list = [int(d) for d in s]
            
        return sum(digit_list)

    return sorted(nums, key=weight)

# --- Implementation 3: Functional/Map Approach (Less common, purely illustrative) ---
def gemini_sd_pass3(nums: list[int]) -> list[int]:
    """Sorts using map and functional decomposition for weight calculation."""
    
    def weight(x: int) -> int:
        s = str(x)
        if not s.startswith('-'):
            # Positive number: standard digit sum
            return sum(map(int, s))
        else:
            # Negative number: negate first digit, sum remaining positive digits
            first_digit_weight = -int(s[1])
            remaining_weight = sum(map(int, s[2:]))
            return first_digit_weight + remaining_weight

    return sorted(nums, key=weight)