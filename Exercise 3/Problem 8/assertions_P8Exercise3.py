# Let `text` be the input string and `res` be the expected output of split_words(text).

# Branch predicates
has_whitespace = any(c.isspace() for c in text)
has_comma = ("," in text)
no_ws_no_comma = (not has_whitespace and not has_comma)

# 1. Exactly one of the three branch conditions applies
assert has_whitespace or has_comma or no_ws_no_comma
#assert not (has_whitespace and has_comma)----------------------INCORRECT-----
assert not (has_whitespace and no_ws_no_comma)
assert not (has_comma and no_ws_no_comma)

# 2. Type of `res` depends on which branch holds
if has_whitespace:
    assert isinstance(res, list)
elif has_comma:
    assert isinstance(res, list)
else:
    assert isinstance(res, int)

# 3. If there is whitespace, result is words split on whitespace
if has_whitespace:
    # text.split() returns maximal non-whitespace substrings
    assert res == text.split()

# 4. If there is no whitespace but there is a comma, split on commas
if (not has_whitespace) and has_comma:
    assert res == text.split(",")
    assert len(res) == text.count(",") + 1
    assert all("," not in part for part in res)

# 5. If there is no whitespace and no comma, res counts lowercase letters
#    whose alphabet index (a=0, b=1, ..., z=25) is odd.
if no_ws_no_comma:
    expected = sum(
        1
        for c in text
        if "a" <= c <= "z" and ((ord(c) - ord("a")) % 2 == 1)
    )
    assert res == expected
