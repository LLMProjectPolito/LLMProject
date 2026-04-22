
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
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                result += "-" * count
                count = 0
            else:
                result += "_"
        else:
            result += char
    if count > 0:
        result += "_" * count
    return result

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example ") == "Example_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_many_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces("  Example   ") == "_Example___"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  This   is   a   test  ") == "_This---is---a---test_"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "___"

def test_fix_spaces_spaces_and_other_chars():
    assert fix_spaces("a b   c") == "a_b--c"

def test_fix_spaces_non_ascii():
    assert fix_spaces("你好   世界") == "你好---世界"

def test_fix_spaces_long_string():
    long_string = " " * 100 + "Example" + " " * 100
    assert fix_spaces(long_string) == "_Example_"

def test_fix_spaces_unusual_spaces():
    assert fix_spaces("Example\t  with\n  tabs") == "Example__with--tabs"