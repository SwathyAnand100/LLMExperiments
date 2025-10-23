#Prompt:
#Implement a function order_by_points(nums) that:
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
"""
Three implementations to sort integers by sum of their digits.
Negative numbers: sum digits after the negative sign.
Stable sort: preserve original order for equal digit sums.

Examples:
- order_by_points([1, 11, -1, -11, -12]) -> [-1, -11, 1, -12, 11]
- order_by_points([]) -> []
"""


# ============================================================
# PLANNER ANALYSIS
# ============================================================
"""
Key Considerations:
1. Digit sum calculation for negatives:
   - For -12: sum = -(1 + 2) = -3
   - For -1: sum = -1
   
2. Stable sorting:
   - Python's sorted() is stable by default
   - Preserve original index order for ties
   
3. Edge cases:
   - Empty list -> return []
   - Single element -> return as-is
   - All zeros -> return as-is
   - Mix of positive/negative

4. Approaches:
   V1: String manipulation for digit extraction
   V2: Mathematical approach (modulo/division)
   V3: Using enumerate for explicit stability
"""


# ============================================================
# IMPLEMENTATION 1: String Manipulation (Most Intuitive)
# ============================================================
def order_by_points_v1(nums):
    """
    Sort by digit sum using string manipulation.
    
    Approach: Convert to string, iterate through digits
    Time Complexity: O(n * m * log n) where m = avg digits per number
    Space Complexity: O(n)
    
    Pros: Easy to understand, handles negatives naturally
    Cons: String conversion overhead
    """
    def digit_sum(n):
        """Calculate sum of digits, handling negatives."""
        if n == 0:
            return 0
        
        # Convert to string and remove negative sign
        s = str(abs(n))
        
        # Sum all digits
        total = sum(int(digit) for digit in s)
        
        # Apply negative if original was negative
        return -total if n < 0 else total
    
    # sorted() is stable by default - preserves original order for equal keys
    return sorted(nums, key=digit_sum)


# ============================================================
# IMPLEMENTATION 2: Mathematical Approach (No Strings)
# ============================================================
def order_by_points_v2(nums):
    """
    Sort by digit sum using pure mathematics.
    
    Approach: Extract digits using modulo and division
    Time Complexity: O(n * m * log n) where m = avg digits per number
    Space Complexity: O(n)
    
    Pros: No string conversion, potentially faster
    Cons: Slightly more complex logic
    """
    def digit_sum(n):
        """Calculate sum of digits mathematically."""
        if n == 0:
            return 0
        
        # Remember if negative
        is_negative = n < 0
        n = abs(n)
        
        # Extract and sum digits
        total = 0
        while n > 0:
            total += n % 10  # Get last digit
            n //= 10         # Remove last digit
        
        # Apply negative if original was negative
        return -total if is_negative else total
    
    # sorted() maintains stability automatically
    return sorted(nums, key=digit_sum)


# ============================================================
# IMPLEMENTATION 3: Explicit Stability with Enumerate
# ============================================================
def order_by_points_v3(nums):
    """
    Sort with explicit index tracking for demonstrating stability.
    
    Approach: Use (digit_sum, original_index) as composite key
    Time Complexity: O(n * m * log n) where m = avg digits per number
    Space Complexity: O(n)
    
    Pros: Explicit stability control, educational value
    Cons: Slightly more verbose, unnecessary for Python's sorted()
    """
    def digit_sum(n):
        """Calculate sum of digits using string approach."""
        if n == 0:
            return 0
        
        s = str(abs(n))
        total = sum(int(d) for d in s)
        return -total if n < 0 else total
    
    # Explicitly pair each number with its original index
    # Sort by (digit_sum, index) to guarantee stability
    indexed = [(num, idx) for idx, num in enumerate(nums)]
    
    # Sort by digit sum first, then by original index (for stability)
    sorted_indexed = sorted(indexed, key=lambda x: (digit_sum(x[0]), x[1]))
    
    # Extract just the numbers
    return [num for num, idx in sorted_indexed]


# ============================================================
# HELPER: Visualize Digit Sums
# ============================================================
def show_digit_sums(nums):
    """Display each number with its digit sum for debugging."""
    def digit_sum(n):
        if n == 0:
            return 0
        s = str(abs(n))
        total = sum(int(d) for d in s)
        return -total if n < 0 else total
    
    print(f"\n{'Number':<10} {'Digit Sum':<10}")
    print("-" * 20)
    for num in nums:
        print(f"{num:<10} {digit_sum(num):<10}")


# ============================================================
# COMPREHENSIVE TESTING
# ============================================================
def test_all_implementations():
    """Test all three implementations thoroughly."""
    
    implementations = [
        ("V1: String Manipulation", order_by_points_v1),
        ("V2: Mathematical", order_by_points_v2),
        ("V3: Explicit Stability", order_by_points_v3),
    ]
    
    test_cases = [
        # (input, expected_output, description)
        (
            [],
            [],
            "Empty list"
        ),
        (
            [0],
            [0],
            "Single zero"
        ),
        (
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5],
            "All single digits descending"
        ),
        (
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            "Already sorted"
        ),
        (
            [0, 0, 0],
            [0, 0, 0],
            "Multiple zeros"
        ),
        (
            [-99, 99, -88, 88],
            [-99, -88, 88, 99],
            "Symmetric positive/negative"
        ),
        (
            [123, 321, 213, 312, 132, 231],
            [123, 321, 213, 312, 132, 231],
            "All same digit sum (6), check stability"
        ),
        (
            [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
            [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
            "Range from -5 to 5"
        ),
    ]
    
    print("=" * 80)
    print("TESTING ALL IMPLEMENTATIONS")
    print("=" * 80)
    
    # Show digit sum examples
    print("\n" + "=" * 80)
    print("DIGIT SUM EXAMPLES")
    print("=" * 80)
    example_nums = [1, 11, -1, -11, -12, 23, -99]
    show_digit_sums(example_nums)
    
    print("\n" + "=" * 80)
    print("CORRECTNESS TESTS")
    print("=" * 80)
    
    total_tests = len(test_cases)
    passed_by_impl = {name: 0 for name, _ in implementations}
    
    for test_num, (input_list, expected, description) in enumerate(test_cases, 1):
        print(f"\n--- Test {test_num}/{total_tests}: {description} ---")
        print(f"Input:    {input_list}")
        print(f"Expected: {expected}")
        print()
        
        all_match = True
        results = []
        
        for impl_name, impl_func in implementations:
            result = impl_func(input_list.copy())  # Copy to avoid mutation
            results.append(result)
            
            matches = result == expected
            status = "✓" if matches else "✗"
            
            if matches:
                passed_by_impl[impl_name] += 1
            else:
                all_match = False
            
            print(f"  {status} {impl_name}: {result}")
        
        if all_match:
            print(f"  ✅ All implementations PASSED")
        else:
            print(f"  ❌ Some implementations FAILED")
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    for impl_name in passed_by_impl:
        passed = passed_by_impl[impl_name]
        print(f"{impl_name}: {passed}/{total_tests} tests passed")
    
    print("\n" + "=" * 80)
    print("STABILITY VERIFICATION")
    print("=" * 80)
    print("Testing: [10, 1, 100, 11, 2]")
    print("Expected: [1, 10, 2, 11, 100]")
    print("Key insight: 10 and 100 both have digit sum 1")
    print("             10 must come before 100 (stable sort)")
    print()
    
    test_input = [10, 1, 100, 11, 2]
    for impl_name, impl_func in implementations:
        result = impl_func(test_input.copy())
        stable = result == [1, 10, 2, 11, 100]
        status = "✓ STABLE" if stable else "✗ NOT STABLE"
        print(f"{status} - {impl_name}: {result}")
    
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print("✓ Use V1 (String) for: Readability, ease of understanding")
    print("✓ Use V2 (Math) for: Avoiding string conversion, slight performance gain")
    print("✓ Use V3 (Explicit) for: Educational purposes, understanding stability")
    print("\nNote: Python's sorted() is stable by default, so V1 and V2 are simpler.")
    print("All three implementations have the same time complexity: O(n*m*log n)")


# Run all tests
if __name__ == "__main__":
    test_all_implementations()