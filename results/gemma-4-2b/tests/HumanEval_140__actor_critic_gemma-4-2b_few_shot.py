
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
                result += "-"
                count = 0
            else:
                result += "_"
        else:
            result += char
    return result

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_single_space():
    assert fix_spaces(" ") == "_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("  ") == "__"

def test_fix_spaces_leading_spaces():
    assert fix_spaces("   ") == "___"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces(" ") == "_"

def test_fix_spaces_mixed_spaces_and_other_chars():
    assert fix_spaces("a b c d") == "a_b_c_d"

def test_fix_spaces_complex_case():
    assert fix_spaces("  This   is   a   test  ") == "_This_is_-a_-test_"

def test_fix_spaces_numbers():
    assert fix_spaces("1 2 3") == "1_2_3"

def test_fix_spaces_special_chars():
    assert fix_spaces("a b c! d") == "a_b_c!_d"

def test_fix_spaces_only_spaces_and_hyphens():
    assert fix_spaces("---   ---") == "---- ---"

def test_fix_spaces_spaces_and_hyphens_mixed():
    assert fix_spaces("a---b   c-d") == "a-b_c-d"

def test_fix_spaces_numbers_with_spaces():
    assert fix_spaces("1 2 3 4 5") == "1_2_3_4_5"

def test_fix_spaces_long_string():
    assert fix_spaces("This is a very long string with many spaces and hyphens.  ---   ---  ") == "This_is_a_very_long_string_with_many_spaces_and_hyphens__---___---"

def test_fix_spaces_all_hyphens():
    assert fix_spaces("----------") == "----------"