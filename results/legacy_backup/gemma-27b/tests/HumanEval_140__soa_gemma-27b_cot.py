import pytest

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_multiple_spaces_at_beginning():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_multiple_spaces_at_end():
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_multiple_spaces_in_middle():
    assert fix_spaces("Example   123   4") == "Example-123-4"

def test_consecutive_spaces_exactly_three():
    assert fix_spaces("abc   def") == "abc-def"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_mixed_spaces():
    assert fix_spaces("  a b  c   d ") == "-a_b-c-d-"

def test_string_with_tabs():
    assert fix_spaces("a\tb\tc") == "a_b_c"

def test_string_with_newlines():
    assert fix_spaces("a\nb\nc") == "a_b_c"

def test_string_with_carriage_returns():
    assert fix_spaces("a\rb\rc") == "a_b_c"

def test_long_string_with_multiple_space_groups():
    long_string = "This is a very long string with   multiple    space groups and some  single spaces."
    expected_string = "This_is_a_very_long_string_with-multiple-space_groups_and_some-single_spaces."
    assert fix_spaces(long_string) == expected_string