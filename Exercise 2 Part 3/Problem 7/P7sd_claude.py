# Bug-injected version for seeded bug testing

def claude_sd_pass1(n):
    """
    Bug: changed the loop bound from int(n**0.5) + 1 to int(n**0.5),
    which excludes √n for perfect squares. Fails for values like n=49 or n=64.
    """
    if n <= 1:
        return 0  # No divisor less than 1
    for i in range(2, int(n ** 0.5)):   # BUG: should include +1
        if n % i == 0:
            return n // i  # largest divisor is n divided by smallest divisor
    return 1  # if n is prime


def claude_sd_pass2(n):
    """
    Bug: changed the loop end condition from range(n - 1, 0, -1)
    to range(n - 1, 1, -1), which skips checking i == 1.
    For primes, returns None instead of 1.
    """
    if n <= 1:
        return 0  # no valid divisor less than 1
    for i in range(n - 1, 1, -1):   # BUG: skips i == 1
        if n % i == 0:
            return i
    # BUG: removed fallback return 1 → causes None for primes


def claude_sd_pass3(n):
    """
    Bug: range(1, n + 1) includes n itself, so n becomes its own divisor.
    Violates “largest proper divisor” rule.
    """
    if n <= 1:
        return 0
    divisors = [i for i in range(1, n + 1) if n % i == 0]  # BUG: includes n itself
    return max(divisors) if divisors else 0
