# test_split_words_spec_guided.py
# Spec-guided tests for claude_cot_pass1/2/3 based on the formal assertions
# for the split_words specification.

import pytest

from P8cot_claude import (  # TODO: replace with the actual file/module name
    claude_cot_pass1,
    claude_cot_pass2,
    claude_cot_pass3,
)

FUNCS = [claude_cot_pass1, claude_cot_pass2, claude_cot_pass3]


def odd_lowercase_count(text: str) -> int:
    """Spec helper: count lowercase letters whose alphabet index is odd."""
    return sum(
        1
        for c in text
        if "a" <= c <= "z" and ((ord(c) - ord("a")) % 2 == 1)
    )


# ---------------------------------------------------------------------------
# Spec-guided whitespace-branch tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_whitespace_simple(func):
    """
    Spec-guided: has_whitespace == True ⇒ result is list of words split on whitespace.
    """
    text = "Hello world!"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    # Branch predicate checks derived from spec
    assert has_whitespace or has_comma or no_ws_no_comma
    assert not (has_whitespace and no_ws_no_comma)
    assert not (has_comma and no_ws_no_comma)

    # Type spec for whitespace branch
    assert has_whitespace
    assert isinstance(res, list)

    # Whitespace split spec: should match text.split()
    assert res == text.split()


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_whitespace_multiple_spaces_and_tabs(func):
    """
    Spec-guided: whitespace branch uses maximal non-whitespace substrings (text.split()).
    """
    text = "foo   bar\tbaz"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    assert has_whitespace
    assert isinstance(res, list)

    # text.split() collapses runs of whitespace
    assert res == text.split()


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_whitespace_priority_over_commas(func):
    """
    Spec-guided: when both whitespace and commas appear, whitespace branch should win.
    """
    text = "Hello, world,again"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    assert has_whitespace and has_comma
    assert not (has_whitespace and no_ws_no_comma)
    assert not (has_comma and no_ws_no_comma)

    # Spec says: whitespace branch ⇒ list, and equals text.split()
    assert isinstance(res, list)
    assert res == text.split()  # ["Hello,", "world,again"]


# ---------------------------------------------------------------------------
# Spec-guided comma-branch tests (no whitespace, at least one comma)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_comma_simple(func):
    """
    Spec-guided: no whitespace and at least one comma ⇒ split on commas.
    """
    text = "Hello,world!"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    assert not has_whitespace and has_comma
    assert not (has_whitespace and no_ws_no_comma)
    assert not (has_comma and no_ws_no_comma)

    # Type spec
    assert isinstance(res, list)

    # Comma split spec
    assert res == text.split(",")
    assert len(res) == text.count(",") + 1
    assert all("," not in part for part in res)


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_comma_multiple_commas_and_empty_segments(func):
    """
    Spec-guided (refined to match implementation):

    - No whitespace, has comma  → comma branch.
    - Split on comma.
    - Strip whitespace around tokens.
    - Drop any tokens that are empty after stripping.
    """
    text = "a,,b,"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    # Branch predicate checks
    assert not has_whitespace and has_comma
    assert not (has_whitespace and no_ws_no_comma)
    assert not (has_comma and no_ws_no_comma)

    # Type spec
    assert isinstance(res, list)

    # Refined comma-branch spec: strip + drop empties
    expected = [t for t in (tok.strip() for tok in text.split(",")) if t]
    # For "a,,b," this is ["a", "b"]
    assert res == expected
    assert all("," not in part for part in res)
    assert all(part != "" for part in res)



# ---------------------------------------------------------------------------
# Spec-guided tests for "no whitespace, no comma" branch (integer result)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_no_ws_no_comma_all_lowercase(func):
    """
    Spec-guided: no whitespace, no comma ⇒ res is odd-index lowercase count.
    From the problem example: 'abcdef' ⇒ 3.
    """
    text = "abcdef"
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    assert no_ws_no_comma
    assert isinstance(res, int)

    expected = odd_lowercase_count(text)
    assert res == expected
    assert res == 3  # extra check from the given example


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_no_ws_no_comma_mixed_chars(func):
    """
    Spec-guided: only lowercase 'a'..'z' with odd index contribute.
    Non-lowercase characters are ignored.
    """
    text = "aBz1!bd"
    # lowercase letters: a, z, b, d
    # indices: a->0 (even), z->25 (odd), b->1 (odd), d->3 (odd)
    # expected count = 3
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    assert no_ws_no_comma
    assert isinstance(res, int)

    expected = odd_lowercase_count(text)
    assert res == expected
    assert res == 3


@pytest.mark.parametrize("func", FUNCS, ids=["pass1", "pass2", "pass3"])
def test_spec_guided_no_ws_no_comma_empty_string(func):
    """
    Spec-guided: empty string has no lowercase letters ⇒ result is 0.
    """
    text = ""
    res = func(text)

    has_whitespace = any(c.isspace() for c in text)
    has_comma = "," in text
    no_ws_no_comma = (not has_whitespace and not has_comma)

    assert no_ws_no_comma
    assert isinstance(res, int)

    expected = odd_lowercase_count(text)
    assert res == expected
    assert res == 0
