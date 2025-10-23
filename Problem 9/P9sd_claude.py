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

def claude_sd_pass1(nums):
    def weight(x):
        s = str(x)
        if s[0] == '-':
            first_digit = -int(s[1])
            remaining_digits = sum(int(d) for d in s[2:])
            return first_digit + remaining_digits
        else:
            return sum(int(d) for d in s)
    return sorted(nums, key=weight)


# Implementation 2: Using lambda directly in sorted
def claude_sd_pass2(nums):
    return sorted(nums, key=lambda x: (-int(str(x)[1]) + sum(int(d) for d in str(x)[2:])
                                       if str(x)[0] == '-' else sum(int(d) for d in str(x))))


# Implementation 3: Precompute weights and use enumerate for stable sorting
def claude_sd_pass3(nums):
    weighted = [(i, n, -int(str(n)[1]) + sum(int(d) for d in str(n)[2:]) if str(n)[0] == '-' else sum(int(d) for d in str(n)))
                for i, n in enumerate(nums)]
    weighted.sort(key=lambda t: (t[2], t[0]))  # sort by weight, then index
    return [n for i, n, w in weighted]


