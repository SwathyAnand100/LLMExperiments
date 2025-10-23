# Task: Write a function that takes a positive integer n and constructs an array a where a[i] = i^2 - i + 1 for 1 <= i <= n. The function should return the number of triples (a[i], a[j], a[k]) with i < j < k such that their sum is divisible by 3. Instructions:
# Reason step by step about how to construct the array a efficiently.
# Consider how to count all valid triples whose sum is a multiple of 3.
# Think about edge cases, such as very small values of n.
# Reflect on ways to optimize the solution for larger values of n.
# After reasoning through your approach, write the Python function that implements it.


def claude_cot_pass1(n):
    if n < 3:
        return 0

    q = n // 3
    r = n % 3

    # a[i] ≡ 0 (mod 3) exactly when i ≡ 2 (mod 3)
    c0 = q + (1 if r == 2 else 0)   # count of a[i] with remainder 0
    c1 = n - c0                      # rest are remainder 1

    def comb3(x: int) -> int:
        return (x * (x - 1) * (x - 2) // 6) if x >= 3 else 0

    return comb3(c0) + comb3(c1)


def claude_cot_pass2(n):
    remainders = [(i * i - i + 1) % 3 for i in range(1, n + 1)]
    
    # Step 2: Count frequency of each remainder
    count0 = remainders.count(0)
    count1 = remainders.count(1)
    count2 = remainders.count(2)  # will always be 0, but kept for clarity

    # Step 3: Compute number of triples whose sum is divisible by 3
    def comb3(x):
        return (x * (x - 1) * (x - 2)) // 6 if x >= 3 else 0

    total = comb3(count0) + comb3(count1)
    # (0,1,2) type not possible, so skipped
    return total



def claude_cot_pass3(n):
    count0 = n // 3 + (1 if n % 3 == 2 else 0)
    # Remaining indices produce a[i] % 3 = 1
    count1 = n - count0

    # Helper function for combinations of 3
    comb3 = lambda x: (x * (x - 1) * (x - 2)) // 6 if x >= 3 else 0

    # Total valid triples
    return comb3(count0) + comb3(count1)