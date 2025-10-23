# Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that:
# Takes a positive integer n, where for each i(1<=i<=n),a[i] = i^2 -i+1
# Returnd the number of triples(a[i],a[j],a[k]) with i<j<k such that a[i]+a[j]+a[k] is a mutiple of 3.
# In your reasoning, consider:
# How to efficiently construct the array a
# How to count all valid triples where the sum is divisible by 3.
# How to handle edge cases, such as small values of n
# How to optimize your approach for larger n
# After explaining your reasoning, provide your Python function implementation

import math

def nCr(n, r):
    """Calculates nCr (n choose r), returning 0 if n < r."""
    if n < r:
        return 0
    # Use math.comb (Python 3.8+) or direct formula
    return math.comb(n, r) if hasattr(math, 'comb') else (
        math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    )

def gemini_cot_pass1_failed(n):
    if n < 3:
        return 0

    # 1. Calculate C0: Count of a[i] such that a[i] % 3 == 0
    # This occurs when i % 3 == 2 (i.e., i = 2, 5, 8, ...)
    # C0 = floor((n - 2) / 3) + 1 = floor((n + 1) / 3)
    C0 = (n + 1) // 3
    
    # 2. Calculate C1: Count of a[i] such that a[i] % 3 == 1
    # Since C0 + C1 = n (as C2 is 0), C1 = n - C0
    C1 = n - C0
    
    # 3. Calculate total triples: C(C0, 3) + C(C1, 3)
    # Valid sum combinations: (0, 0, 0) and (1, 1, 1)
    
    count_000 = nCr(C0, 3)
    count_111 = nCr(C1, 3)
    
    return count_000 + count_111


#Changed Prompt:
# The previous code generated is incorrect. Recheck your code. Explain step-by-step how you would solve the following problem before writing any code:
# Create a function that:
# Takes a positive integer n,
# Constructs an interger array a of length n, where for each i(1<=1<=n), a[i] = i^2 - i + 1
# Return the number of triples (a[i],a[j],a[k]) with i<j<k such that a[i]+a[j]+a[k] is a multiple of 3. In your reasoning,consider:
# How to construct the array a and analyze the possible remainders of a[i] modulo 3.
# How to count the number of elements in each remainder class (0, 1, 2) modulo 3.
# Which combinations of three elements (by remainder) will sum to a multiple of 3.
# How to efficiently count the number of valid triples using combinatorial formulas.
# How to handle edge cases, such as small values of n 
# After explaining your reasoning, provide your Python function implementation.


import math

def gemini_cot_pass1(n: int) -> int:
    # 1. Edge Case: Cannot form a triple if n < 3
    if n < 3:
        return 0

    # Helper function for combinations (n choose r)
    def nCr(m, r):
        if m < r:
            return 0
        # math.comb is the standard, efficient way to calculate combinations
        return math.comb(m, r)

    # 2. Calculate Remainder Counts (O(1))
    
    # C0: Count of a[i] such that a[i] % 3 == 0 (occurs when i % 3 == 2)
    # Formula: C0 = floor((n + 1) / 3)
    C0 = (n + 1) // 3
    
    # C1: Count of a[i] such that a[i] % 3 == 1 (occurs when i % 3 == 0 or 1)
    C1 = n - C0
    
    # 3. Calculate Total Valid Triples (O(1))
    
    # Valid combinations: (0, 0, 0) and (1, 1, 1)
    count_000 = nCr(C0, 3)
    count_111 = nCr(C1, 3)
    
    return count_000 + count_111


def gemini_cot_pass2(n: int) -> int:
    if n < 3:
        return 0

    # Initialize counts for remainders 0, 1, 2
    counts = [0, 0, 0] # counts[r] = Cr
    
    # 1. Iterate and Count (O(n))
    for i in range(1, n + 1):
        # The remainder of a[i] = i^2 - i + 1 is determined by i % 3:
        # If i % 3 == 2, remainder is 0.
        # If i % 3 == 0 or 1, remainder is 1.
        
        # We can calculate the remainder directly to verify the pattern:
        # Note: (i*i - i + 1) % 3 is equivalent to the analysis.
        remainder = (i * i - i + 1) % 3
        counts[remainder] += 1
            
    C0 = counts[0]
    C1 = counts[1]
    
    # 2. Calculate Total Triples (O(1))
    def nCr(m, r):
        if m < r: return 0
        return math.comb(m, r)

    # Valid combinations: (0, 0, 0) and (1, 1, 1)
    return nCr(C0, 3) + nCr(C1, 3)



def gemini_cot_pass3(n: int) -> int:
    if n < 3:
        return 0

    # 1. Construct the array of remainders a[i] % 3 (O(n))
    a_remainders = []
    for i in range(1, n + 1):
        # Calculate a[i] = i^2 - i + 1 and take the remainder
        remainder = (i * i - i + 1) % 3
        a_remainders.append(remainder)
        
    count = 0
    
    # 2. Iterate through all ordered triples (i, j, k) (O(n^3))
    # Note: Indices in Python are 0-based, so they range from 0 to n-1.
    N = len(a_remainders)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                # Check if the sum of remainders is a multiple of 3
                if (a_remainders[i] + a_remainders[j] + a_remainders[k]) % 3 == 0:
                    count += 1
                    
    return count