# test_Iter1_P7.py

import pytest
from P7sd_claude import claude_sd_pass1, claude_sd_pass2, claude_sd_pass3

FUNCS = [claude_sd_pass1, claude_sd_pass2, claude_sd_pass3]

CASES = [
    (0,0),
    (100, 50),  # even composite fast path: smallest factor=2 => return n//2
    (45, 15),   # odd composite loop hit: factor 3 found early
    (27, 9),    # odd composite loop hit: factor 3 with higher power (3^3)
]

@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
@pytest.mark.parametrize(
    "n, expected",
    CASES,
    ids=[
        "n=0_guard",
        "n=100_even_fast",
        "n=45_odd_loop",
        "n=27_odd_power3",
    ],
)
def test_largest_proper_divisor_minimal(func, n, expected):
    assert func(n) == expected
