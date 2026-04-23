
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
                result += "-"
                space_count = 0
            else:
                result += "_"
        else:
            result += char
    return result

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_multiple_spaces():
    assert fix_spaces("Example   ") == "Example---"

def test_leading_spaces():
    assert fix_spaces(" Example ") == "_Example_"

def test_trailing_spaces():
    assert fix_spaces(" Example ") == "_Example_"

def test_mixed_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_string_with_special_characters():
    assert fix_spaces("Hello, world!") == "Hello,_world!"

def test_string_with_numbers():
    assert fix_spaces("123 456") == "123_456"