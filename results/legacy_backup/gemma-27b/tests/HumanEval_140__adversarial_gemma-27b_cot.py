import pytest

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_trailing_space():
    assert fix_spaces("Example 4 ") == "Example_4_"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example 5 ") == "_Example_5_"

def test_multiple_leading_spaces():
    assert fix_spaces("   Example 6") == "---Example_6"

def test_multiple_trailing_spaces():
    assert fix_spaces("Example 7   ") == "Example_7---"

def test_multiple_spaces_in_middle():
    assert fix_spaces("Example   8   9") == "Example-8-9"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "---"

def test_mixed_spaces():
    assert fix_spaces("  Example    123   ") == "--Example-123---"

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example\t1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example\n1"

def test_long_string_with_many_spaces():
    long_string = "This is a very long string with " + "   " * 5 + "many spaces."
    expected_string = "This_is_a_very_long_string_with-----many_spaces."
    assert fix_spaces(long_string) == expected_string