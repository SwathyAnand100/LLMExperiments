# Task:
# Write a function that accepts a positive integer n and returns the largest integer less than n that divides n evenly (i.e., the greatest proper divisor of n).	Instructions:
# Step through how to find divisors of n efficiently, avoid checking every number from 1 to n-1 when possible.
# Consider using properties of divisors (pairs around sqrt(n)) to reduce work and identify the largest proper divisor quickly.
# Decide what the function should return for small values like n = 1 or n = 2 (where no proper divisor greater than 0 exists) and document that behavior.
# Think about edge cases (non-positive input, prime numbers where the largest proper divisor is 1, perfect squares, very large n) and how your algorithm handles them.
# After reasoning step-by-step, implement a clear, efficient Python function that returns the largest divisor less than n.
# Include brief comments or notes explaining why the chosen approach is correct and how it addresses the edge cases.

import math

def claude_cot_pass1(n):
    if n <= 1:
        return None
    # iterate downward and return first divisor found
    for d in range(n - 1, 0, -1):
        if n % d == 0:
            return d
    # logically unreachable for n > 1, because d=1 always divides n
    return None

def claude_cot_pass2(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return n // 2  # smallest factor is 2 -> largest proper divisor is n//2

    limit = math.isqrt(n)
    # check odd factors 3,5,7,...
    for f in range(3, limit + 1, 2):
        if n % f == 0:
            # f is smallest factor > 1, so other factor n//f is the largest proper divisor
            return n // f

    # no factor found => n is prime
    return 1

def claude_cot_pass3(n):
    if n <= 1:
        return None
    # handle 2 separately
    if n % 2 == 0:
        return n // 2

    # try odd candidates up to sqrt(n)
    limit = math.isqrt(n)
    f = 3
    while f <= limit:
        if n % f == 0:
            return n // f
        f += 2
    # prime
    return 1