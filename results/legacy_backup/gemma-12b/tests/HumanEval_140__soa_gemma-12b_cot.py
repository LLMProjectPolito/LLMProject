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

def test_multiple_spaces_at_beginning():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_multiple_spaces_at_end():
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_multiple_spaces_in_middle():
    assert fix_spaces("Example  6  7") == "Example_6-7"

def test_mixed_spaces():
    assert fix_spaces(" Example  8   9") == "_Example-8-9"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_string_with_multiple_spaces():
    assert fix_spaces("This is a very long string with   multiple    spaces.") == "This_is_a_very_long_string_with-multiple-spaces."

def test_string_with_tabs_and_spaces():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines_and_spaces():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_special_characters_and_spaces():
    assert fix_spaces("!@#$%^&*() Example 1") == "!@#$%^&*()_Example_1"

def test_string_with_unicode_characters_and_spaces():
    assert fix_spaces("你好 Example 1") == "你好_Example_1"