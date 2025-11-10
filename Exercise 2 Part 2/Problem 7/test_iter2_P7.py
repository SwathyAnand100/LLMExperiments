# test_Iter1_P7.py
# Purpose: Exercise key decision paths and edge conditions for Largest Proper Divisor.
# Notes:
# - Tests are parametrized across all three implementations and a compact, non-redundant set of inputs.
# - Each case includes a brief comment indicating the targeted branch/condition.

import pytest
from P7sd_claude import claude_sd_pass1, claude_sd_pass2, claude_sd_pass3


FUNCS = [claude_sd_pass1, claude_sd_pass2, claude_sd_pass3]

CASES = [
    (0, 0),    # guard n<=1: zero input
    (1, 0),    # guard n<=1: one input

    (100, 50), # even composite fast path: halve even n

    (45, 15),  # odd composite (factor found in loop): mixed factors (3*3*5)
    (27, 9),   # odd composite (factor found in loop): power of a single prime (3^3)

    (13, 1),   # prime fallback: small prime
    (97, 1),   # prime fallback: larger prime

    (49, 7),   # perfect square boundary (isqrt): odd square (7*7)
    (64, 32),  # perfect square boundary (isqrt): even square; also power of two

    (2, 1),    # small single-digit edge: minimal even prime
    (3, 1),    # small single-digit edge: minimal odd prime
]


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
@pytest.mark.parametrize(
    "n, expected",
    CASES,
    ids=[
        "n=0_guard",
        "n=1_guard",
        "n=100_even_fast",
        "n=45_odd_loop",
        "n=27_odd_power3",
        "n=13_prime",
        "n=97_prime",
        "n=49_square_isqrt",
        "n=64_square_even",
        "n=2_small_edge",
        "n=3_small_edge",
    ],
)
def test_largest_proper_divisor(func, n, expected):
    assert func(n) == expected
