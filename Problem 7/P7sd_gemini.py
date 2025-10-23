#Write code for a function largest_divisor(n) that takes an integer n and returns the largest number less than n that divides n evenly.
# Consider how to efficiently find the largest divisor for any positive integer n.
# Think about what should be returned for small values of n, such as 1 or 2.
# Consider edge cases and how to handle them.. After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes. 
# Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.

import math

def gemini_sd_pass1(n: int) -> int:
    """
    Implementation 1: O(sqrt(n)) - Finds the largest divisor using the smallest factor.
    The largest divisor (d < n) = n / smallest_factor(n, >1).
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be a positive integer greater than 1.")

    # Optimization 1: Check for the smallest factor 2
    if n % 2 == 0:
        return n // 2

    # Optimization 2: Check for odd factors up to sqrt(n)
    i = 3
    # Use math.isqrt for potentially better performance with large integers
    limit = math.isqrt(n) 
    
    while i <= limit:
        if n % i == 0:
            # i is the smallest factor > 1 found so far
            return n // i
        i += 2
        
    # If no factors are found, n is prime, and the largest divisor is 1.
    return 1


def gemini_sd_pass2(n: int) -> int:
    """
    Implementation 2: O(n) - Brute force approach by iterating downwards from n-1.
    The first divisor found is guaranteed to be the largest.
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be a positive integer greater than 1.")

    # Iterate from n-1 down to 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
            
    # This line should technically only be reached if n=1, but the check handles it.
    # We return 1 just in case, though the loop structure guarantees a return.
    return 1


def gemini_sd_pass3(n: int) -> int:
    """
    Implementation 3: O(sqrt(n)) - Finds divisors by iterating up to sqrt(n)
    and storing the largest complement (n/i).
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be a positive integer greater than 1.")
        
    largest_complement = 1
    limit = math.isqrt(n)

    # Iterate from 2 up to the square root of n
    for i in range(2, limit + 1):
        if n % i == 0:
            # i is a factor. n // i is the corresponding complement factor.
            # Since i <= sqrt(n), n // i >= sqrt(n).
            # This complement is likely the largest non-trivial divisor.
            largest_complement = n // i
            
            # Since we iterate upwards, the FIRST factor 'i' found will give the
            # LARGEST complement 'n // i'. We can stop immediately.
            return largest_complement

    # If the loop finishes, n is prime, or the only factor found was 1 (which we skipped).
    # The largest divisor must be 1.
    return 1