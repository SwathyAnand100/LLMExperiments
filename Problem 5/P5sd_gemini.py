#Write code for a function that:
# Takes a positive integer n, where for each i(1<=i<=n),a[i] = i^2 -i+1
# Returnd the number of triples(a[i],a[j],a[k]) with i<j<k such that a[i]+a[j]+a[k] is a mutiple of 3.
# In your reasoning, consider :
# How to construct the array a and analyze the possible remainders of a[i] modulo 3.
# How to count the number of elements in each remainder class (0, 1, 2) modulo 3.
# Which combinations of three elements (by remainder) will sum to a multiple of 3.
# How to efficiently count the number of valid triples using combinatorial formulas.
# How to handle edge cases, such as small values of n 
# After explaining your reasoning, provide your Python function implementation.
#  After implementing your initial solution, review your approach by identifying any potential issues, edge cases, or mistakes. 
# Debug your own solution, correcting any flaws you find. Finally, state the rationale for your final, corrected answer along with the code.

def combinations(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # Optimization: C(n, k) = C(n, n-k)
    if k > n // 2:
        k = n - k
    
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res

def gemini_sd_pass1(n):
    if n < 3:
        # A triple requires at least 3 elements.
        return 0

    # 1. Calculate A: Count of indices i (1 <= i <= n) where a[i] is 0 mod 3.
    # This occurs iff i is 2 mod 3 (i = 2, 5, 8, ...).
    q = n // 3
    r = n % 3
    
    # A is the count of i such that i = 3k + 2
    if r == 2:
        A = q + 1
    else: # r == 0 or r == 1
        A = q

    # 2. Calculate B: Count of indices i where a[i] is 1 mod 3.
    # This occurs iff i is 0 mod 3 or 1 mod 3.
    B = n - A

    # 3. Calculate total triples: C(A, 3) + C(B, 3).
    # The required sum is a multiple of 3 iff all remainders are 0 or all are 1.
    count_A = combinations(A, 3)
    count_B = combinations(B, 3)
    
    return count_A + count_B


def combinations_n_choose_3(n: int) -> int:
    """Calculates C(n, 3) = n * (n - 1) * (n - 2) / 6. Returns 0 if n < 3."""
    if n < 3:
        return 0
    # Use integer division since the result is guaranteed to be an integer.
    return n * (n - 1) * (n - 2) // 6


def gemini_sd_pass2(n):
    if n < 3:
        return 0

    # Remainder Analysis: a[i] is 0 mod 3 iff i is 2 mod 3.
    # Otherwise, a[i] is 1 mod 3.
    
    # 1. Calculate A: Count of indices i (1 <= i <= n) where i is 2 mod 3.
    
    q = n // 3
    r = n % 3
    
    # Indices 2, 5, 8, ...
    if r == 2:
        A = q + 1
    else: 
        A = q

    # 2. Calculate B: Count of indices i where i is NOT 2 mod 3 (i.e., 0 or 1 mod 3).
    B = n - A

    # 3. Valid Sums: Must be (0, 0, 0) or (1, 1, 1) mod 3.
    # Total Triples = C(A, 3) + C(B, 3)
    count_A = combinations_n_choose_3(A)
    count_B = combinations_n_choose_3(B)
    
    return count_A + count_B


def combinations_n_choose_3_new(n: int) -> int:
    """Calculates C(n, 3) = n * (n - 1) * (n - 2) / 6. Returns 0 if n < 3."""
    if n < 3:
        return 0
    return n * (n - 1) * (n - 2) // 6


def gemini_sd_pass3(n):
    if n < 3:
        return 0

    # A: Count of a[i] congruent to 0 mod 3 (i.e., i mod 3 == 2)
    # B: Count of a[i] congruent to 1 mod 3 (i.e., i mod 3 == 0 or 1)
    A = 0
    B = 0
    
    # Iterate through all indices i from 1 to n to count remainder classes
    for i in range(1, n + 1):
        # We only need to check i mod 3.
        # i^2 - i + 1 mod 3 is 0 iff i mod 3 is 2.
        if i % 3 == 2:
            A += 1
        else: # i mod 3 is 0 or 1
            B += 1

    # Validation: A + B should always equal n
    # assert A + B == n

    # The required sum is a multiple of 3 iff all three elements are 0 mod 3 (C(A, 3))
    # OR all three elements are 1 mod 3 (C(B, 3)).
    count_A = combinations_n_choose_3_new(A)
    count_B = combinations_n_choose_3_new(B)
    
    return count_A + count_B

