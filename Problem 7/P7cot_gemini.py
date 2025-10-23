# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that takes an integer n and returns the largest number less than n that divides n evenly.
# Consider how to efficiently find the largest divisor for any positive integer n.
# Think about what should be returned for small values of n, such as 1 or 2.
# Consider edge cases and how to handle them.
# After explaining your reasoning, provide your Python function implementation.

import math

def gemini_cot_pass1(n: int) -> int:
    if not isinstance(n, int) or n <= 1:
        # Edge case: No positive integer strictly less than n divides n.
        return 0
    
    # Iterate from 2 up to the integer part of the square root of n
    limit = int(math.sqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            # i is the smallest factor (> 1). The corresponding largest factor is n // i.
            return n // i
            
    # If the loop finishes, n is prime (or 1, handled above). 
    # The largest proper divisor of a prime number is 1.
    return 1

def gemini_cot_pass2(n: int) -> int:
    if not isinstance(n, int) or n <= 1:
        return 0

    # 1. Handle even numbers immediately
    if n % 2 == 0:
        # If n is even, the smallest factor is 2, and the largest proper divisor is n/2.
        return n // 2
    
    # 2. Iterate only odd numbers from 3 up to the square root of n
    limit = int(math.sqrt(n))
    
    # Start at 3 and step by 2 (checking only odd numbers)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            # i is the smallest odd factor (> 1).
            return n // i
            
    # If no factor is found, n is prime (or 1, handled above).
    return 1

def gemini_cot_pass3(n: int) -> int:
    """
    Finds the largest number less than n that divides n evenly by generating
    all proper divisors and finding the maximum.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    proper_divisors = {1} # Start with 1, as it is always a proper divisor for n > 1
    
    limit = int(math.sqrt(n))
    
    for i in range(2, limit + 1):
        if n % i == 0:
            # Found a factor i
            proper_divisors.add(i)
            
            # Add its cofactor, which is the other factor in the pair (n/i)
            cofactor = n // i
            proper_divisors.add(cofactor)
            
    # Edge case: If n is a perfect square, limit*limit == n, and the loop
    # might add the square root twice, which is fine for a set.
    
    # We want the max divisor that is strictly less than n. 
    # Since we only collected factors up to the square root, and their cofactors,
    # and all cofactors are <= n, we just need to find the max.
    
    # For a composite number, the largest cofactor will be n // smallest_factor > 1.
    # For a prime number, the set is {1}, max is 1.
    return max(proper_divisors)


