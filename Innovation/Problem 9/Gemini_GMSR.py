#Prompt:
# Implement a function order_by_points(nums) that:
# Sorts integers in ascending order based on the sum of their digits.
# If multiple numbers share the same digit sum, retain their original input order (i.e., ensure stable sorting).
# Handle negative integers correctly by considering the digits after the negative sign.
# Examples:
# order_by_points([1, 11, -1, -11, -12]) -> [-1, -11, 1, -12, 11]
# order_by_points([]) -> []
# Agents and Roles:
# 1. Planner- Explain how to compute the digit sum, including negative numbers. Identify stable sorting strategies and edge cases (empty lists, all negatives).
# 2. Solver-Implement the function in Python, ensuring that negative digits are handled correctly and sorting is stable.
# 3. Verifier- Run tests including mixed positive/negative numbers, large values, and empty input. Report if outputs mismatch expected results.
# 4. Refiner- Apply feedback to improve correctness and readability. Provide the final clean implementation with reasoning on how stability was ensured.
# Goal:
# Deliver a final version that handles negatives, maintains input order for ties, and matches expected outputs on all test cases.

def get_digit_sum_string(n: int) -> int:
    """Calculates the sum of digits for an integer 'n', ignoring the sign."""
    # Convert absolute value to string, then sum integer values of digits.
    return sum(int(digit) for digit in str(abs(n)))

# Implementation 1: Refined Pythonic Stable Sort
def order_by_points_1(nums: list[int]) -> list[int]:
    """Sorts integers based on digit sum (ascending) using a stable, pythonic key."""
    # Stability is guaranteed by Python's Timsort algorithm used in sorted().
    return sorted(nums, key=get_digit_sum_string)

# Implementation 2: Mathematical Digit Sum
def get_digit_sum_math(n: int) -> int:
    """Calculates the sum of digits using repeated modulo 10 and division."""
    total = 0
    num = abs(n)
    
    # Handle the case of n=0
    if num == 0:
        return 0

    while num > 0:
        total += num % 10  # Get the last digit
        num //= 10         # Remove the last digit
        
    return total

def order_by_points_2(nums: list[int]) -> list[int]:
    """Sorts integers based on digit sum (ascending) using the mathematical key."""
    return sorted(nums, key=get_digit_sum_math)

# Implementation 3: Explicit Stability Index Key
def order_by_points_3(nums: list[int]) -> list[int]:
    """Sorts using a tuple key (digit_sum, original_index) to explicitly ensure stability."""
    
    # 1. Create a list of tuples: (original_index, number)
    indexed_nums = list(enumerate(nums))
    
    # 2. Define a key function to return (digit_sum, original_index)
    def combined_key(item):
        original_index, number = item
        digit_sum = get_digit_sum_string(number)
        return (digit_sum, original_index)

    # 3. Sort the indexed list. Sorting by the index as the secondary key ensures stability.
    sorted_indexed = sorted(indexed_nums, key=combined_key)
    
    # 4. Extract the numbers from the sorted indexed list
    return [number for _, number in sorted_indexed]

# --- Test Cases ---
TEST_CASES = [
    # Input list, Expected Output (based on stable sorting rule)
    ([], []),
    ([100, 10, 1], [100, 10, 1]), # All sum=1. Stability maintains input order.
    ([-123, 1, 321, 12, -21], [1, 12, -21, -123, 321]), # Sums: 6, 1, 6, 3, 3. Order: 1, 3, 3, 6, 6.
    ([0, -1, 1], [0, -1, 1]) # Sums: 0, 1, 1.
]

# --- Testing Logic ---
print("--- Testing order_by_points Implementations ---")

implementations = {
    "Implementation 1 (Pythonic)": order_by_points_1,
    "Implementation 2 (Math Key)": order_by_points_2,
    "Implementation 3 (Explicit Index Key)": order_by_points_3,
}

for name, func in implementations.items():
    print(f"\nTesting: {name}")
    passed = True
    for input_list, expected in TEST_CASES:
        # Create a copy to ensure the original input is not modified
        input_copy = list(input_list) 
        result = func(input_copy)
        
        if result == expected:
            print(f"  ✅ PASS: Input {input_list} -> Output {result}")
        else:
            print(f"  ❌ FAIL: Input {input_list}")
            print(f"    Expected: {expected}")
            print(f"    Got:      {result}")
            passed = False
            
    if passed:
        print(f"  All tests passed for {name}.")
    else:
        print(f"  Some tests FAILED for {name}.")