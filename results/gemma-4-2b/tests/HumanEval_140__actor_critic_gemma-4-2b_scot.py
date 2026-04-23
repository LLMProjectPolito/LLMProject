
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = ""
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count > 2:
                result += '-'
                space_count = 0
            else:
                result += '_'
        else:
            result += char
    return result


def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_only_spaces():
    assert fix_spaces("   ") == "___"

def test_leading_trailing_spaces():
    assert fix_spaces("  Example  ") == "_Example_"

def test_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_multiple_spaces():
    assert fix_spaces("Example   ") == "_Example--"

def test_mixed_spaces():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example   1") == "_Example--1"

def test_long_string():
    long_string = "This is a very long string with many spaces."
    assert fix_spaces(long_string) == "This_is_a_very_long_string_with_many_spaces."

def test_mixed_whitespace():
    assert fix_spaces("Example\t1") == "Example_1"
    assert fix_spaces("Example\n1") == "Example_1"

def test_very_long_string():
    very_long_string = "a" * 1000 + "b"
    assert fix_spaces(very_long_string) == "a_a_a_a_a_a_a_a_a_a_b"

def test_unicode_spaces():
    assert fix_spaces("Example\u00A01") == "Example_1" # \u00A0 is a non-breaking space

def test_whitespace_only_with_non_whitespace():
    assert fix_spaces(" \t\rExample\n") == "_Example_"

def test_whitespace_only():
    assert fix_spaces(" \t\r\n") == "___"

# Add a note about performance
# @pytest.mark.slow
def test_very_long_string_slow():
    very_long_string = "a" * 10000 + "b"
    assert fix_spaces(very_long_string) == "a_a_a_a_a_a_a_a_a_a_b"