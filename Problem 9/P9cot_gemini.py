# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that sorts a list of integers in ascending order according to the sum of their digits. If multiple numbers have the same digit sum, they should retain their original relative order (i.e., sort is stable).
# Consider how to calculate the sum of digits for each number, including negative numbers.
# Think about how to use a stable sorting method to preserve the original order for ties.
# Consider edge cases, such as empty lists or lists with all numbers having the same digit sum.
# After explaining your reasoning, provide your Python function implementation.

def get_digit_sum_v1(n: int) -> int:
    """Calculates the sum of the digits of an integer (using its absolute value)."""
    abs_n = abs(n)
    return sum(int(digit) for digit in str(abs_n))

def gemini_cot_pass1_failed(numbers: list[int]) -> list[int]:
    """Sorts a list of integers stably based on the ascending sum of their digits."""
    return sorted(numbers, key=get_digit_sum_v1)

#Prompt 2 - it fails because it does not grasp the question, it simply does sorting instead of sorting according to digits.
#New prompt: 
# The task is to implement a Python function order_by_points(nums) that sorts a list of integers.
# Crucially, the provided example reveals a non-standard sorting key calculation.
# Input: [1, 11, -1, -11, -12] Required Output: [-1, -11, 1, -12, 11]
# Step 1: Determine the Sorting Key (Weight) and Tie-breaker Rule.
# Analyze the input and required output to deduce the exact "weight" calculation for each number.
# Example: For the input numbers, we must find a set of keys (weights) that, when sorted, results in the required output:
# 1 (Weight: 1)
# 11 (Weight: 2)
# −1 (Weight: −1)
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
# Provide your reasoning for Step 1, the implementation of the weight function, and the final Python code for order_by_points.

def gemini_cot_pass1(nums: list[int]) -> list[int]:
    """
    Sorts based on a unique 'weight' where the sign is only applied to the first digit.
    The sort is stable for ties.
    """
    if not nums:
        return []

    def weight(x: int) -> int:
        s = str(x)
        if s.startswith('-'):
            # Convert digits after '-' to int, make the first one negative, then sum.
            digits = [int(d) for d in s[1:]]
            if digits:
                digits[0] = -digits[0]
            return sum(digits)
        else:
            # Simple sum of all digits for positive numbers.
            return sum(int(d) for d in s)

    return sorted(nums, key=weight)

def gemini_cot_pass2(nums: list[int]) -> list[int]:
    """
    Sorts using the unique signed-first-digit weight with a conditional list comprehension.
    The sort is stable for ties.
    """
    if not nums:
        return []
    
    return sorted(
        nums, 
        key=lambda n: sum(
            # Apply the sign to the digit only if it's the first digit (i.e., its index is 0) 
            # and the number is negative (n < 0).
            (int(d) if i > 0 or n >= 0 else -int(d)) 
            for i, d in enumerate(str(abs(n))) # Use absolute value string for digit parsing
        )
    )

def _get_signed_weight_math(n: int) -> int:
    """Calculates the unique signed-first-digit weight using mathematical operations."""
    if n == 0:
        return 0
        
    abs_n = abs(n)
    
    # 1. Calculate the magnitude of the highest digit
    power_of_10 = 1
    temp = abs_n // 10
    while temp > 0:
        power_of_10 *= 10
        temp //= 10
        
    # 2. Extract the highest digit
    highest_digit = abs_n // power_of_10
    
    # 3. Calculate the sum of all *other* digits (positive sum)
    remaining_digits_sum = 0
    remaining_num = abs_n % power_of_10
    
    # Mathematical sum of remaining digits
    while remaining_num > 0:
        remaining_digits_sum += remaining_num % 10
        remaining_num //= 10
        
    # 4. Combine: highest digit is signed, others are positive
    if n < 0:
        return -highest_digit + remaining_digits_sum
    else:
        return highest_digit + remaining_digits_sum

def gemini_cot_pass3(nums: list[int]) -> list[int]:
    """
    Sorts based on the unique signed-first-digit weight, calculated mathematically.
    The sort is stable for ties.
    """
    if not nums:
        return []
    
    return sorted(nums, key=_get_signed_weight_math)