import pytest

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_multiple_spaces_and_leading_space():
    assert fix_spaces("  Example   1 2") == "-Example-1_2"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_mixed_spaces():
    assert fix_spaces("A B  C   D") == "A_B--C-D"

def test_long_string_with_multiple_consecutive_spaces():
    assert fix_spaces("This is a very long string with   multiple    consecutive spaces.") == "This_is_a_very_long_string_with--multiple---consecutive_spaces."

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example\t 1 \n 2") == "Example_1__2"