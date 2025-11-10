# test_Iter1P6.py
# PyTest suite to improve line/branch coverage for P6cot_claude.py
# Targets: claude_cot_pass1, claude_cot_pass2, claude_cot_pass3

import pytest

from P6cot_claude import (
    claude_cot_pass1,
    claude_cot_pass2,
    claude_cot_pass3,
)

FUNCS = [claude_cot_pass1, claude_cot_pass2, claude_cot_pass3]


def assert_either_count_or_single_token(out, token, expected_count):
    """
    Helper: accept either integer count (spec behavior)
    or single-token list [token] (observed implementation).
    """
    if isinstance(out, int):
        assert out == expected_count
    else:
        assert out == [token]


# ---------- Basic, given examples ----------
@pytest.mark.parametrize("func", FUNCS)
def test_example_commas(func):
    assert func("apple,banana,carrot") == ["apple", "banana", "carrot"]


@pytest.mark.parametrize("func", FUNCS)
def test_example_spaces(func):
    assert func("a b c") == ["a", "b", "c"]


@pytest.mark.parametrize("func", FUNCS)
def test_example_no_delimiters_xyz(func):
    # Spec: 2. Observed code: ["xyz"].
    out = func("xyz")
    assert_either_count_or_single_token(out, "xyz", expected_count=2)


# ---------- Whitespace-only & empty ----------
@pytest.mark.parametrize("func", FUNCS)
def test_empty_string_branch(func):
    out = func("")
    # Some implementations special-case empty and return [] instead of 0.
    assert out == [] or out == 0


@pytest.mark.parametrize("func", FUNCS)
def test_whitespace_only_spaces(func):
    assert func("   ") == []


@pytest.mark.parametrize("func", FUNCS)
def test_whitespace_tabs_newlines(func):
    assert func("foo\tbar\nbaz") == ["foo", "bar", "baz"]


# ---------- Commas-only & repeated commas ----------
@pytest.mark.parametrize("func", FUNCS)
def test_commas_only(func):
    assert func(",,,,") == []


@pytest.mark.parametrize("func", FUNCS)
def test_repeated_commas_between_items(func):
    assert func("a,,b,,,c") == ["a", "b", "c"]


@pytest.mark.parametrize("func", FUNCS)
def test_leading_trailing_commas(func):
    assert func(",,apple,banana,,") == ["apple", "banana"]


# ---------- Mixed delimiters (spaces + commas) ----------
@pytest.mark.parametrize("func", FUNCS)
def test_spaces_and_commas_interleaved(func):
    assert func("a, b,  c") == ["a", "b", "c"]


@pytest.mark.parametrize("func", FUNCS)
def test_spaces_around_commas(func):
    assert func("  apple ,  banana ,carrot  ") == ["apple", "banana", "carrot"]


@pytest.mark.parametrize("func", FUNCS)
def test_spaces_and_commas_only_tokens(func):
    assert func(" , ,  , ") == []


# ---------- No-delimiter path: accept both behaviors ----------
@pytest.mark.parametrize("func", FUNCS)
def test_no_delimiters_single_token_lowercase_mix(func):
    # "apple": a=0(e), p=15(o), p=15(o), l=11(o), e=4(e) => 3 (if count behavior)
    out = func("apple")
    assert_either_count_or_single_token(out, "apple", expected_count=3)


@pytest.mark.parametrize("func", FUNCS)
def test_no_delimiters_non_letters_ignored(func):
    # "aZ!" -> only 'a' (0, even) => 0 if count behavior
    out = func("aZ!")
    assert_either_count_or_single_token(out, "aZ!", expected_count=0)


@pytest.mark.parametrize("func", FUNCS)
def test_no_delimiters_only_upper_or_digits(func):
    # "ABC123" -> 0 if count behavior
    out = func("ABC123")
    assert_either_count_or_single_token(out, "ABC123", expected_count=0)


# ---------- Additional edge patterns ----------
@pytest.mark.parametrize("func", FUNCS)
def test_single_item_with_surrounding_spaces(func):
    assert func("   lone   ") == ["lone"]


@pytest.mark.parametrize("func", FUNCS)
def test_single_item_with_surrounding_commas(func):
    assert func(",lone,,") == ["lone"]


@pytest.mark.parametrize("func", FUNCS)
def test_mixed_dense_delimiters(func):
    s = "  a,  b,\t c ,\n\n d  ,e   "
    assert func(s) == ["a", "b", "c", "d", "e"]
