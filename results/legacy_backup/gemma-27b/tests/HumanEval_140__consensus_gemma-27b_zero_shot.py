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

def test_multiple_spaces_both_ends():
    assert fix_spaces("   Example   6   ") == "-Example-6-"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_mixed_spaces():
    assert fix_spaces("Example  1 2   3") == "Example-1_2-3"

def test_consecutive_and_single_spaces():
    assert fix_spaces("Example  1 2") == "Example-1_2"

def test_long_string_with_multiple_spaces():
    long_string = "This is a long string with   multiple   spaces and some  single spaces."
    expected_string = "This_is_a_long_string_with-multiple-spaces_and_some-single_spaces."
    assert fix_spaces(long_string) == expected_string

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_carriage_returns():
    assert fix_spaces("Example\r1") == "Example_1"

def test_consecutive_spaces_and_leading():
    assert fix_spaces("  Example 1") == "-Example_1"

def test_consecutive_spaces_and_trailing():
    assert fix_spaces("Example 1  ") == "Example_1-"

def test_long_string_with_mixed_spaces():
    long_string = "This is a long string with   multiple   spaces and some single spaces."
    expected_string = "This_is_a_long_string_with-multiple-spaces_and_some_single_spaces."
    assert fix_spaces(long_string) == expected_string