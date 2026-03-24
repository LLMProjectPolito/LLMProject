
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
    new_text = text.replace(" ", "_")
    while "__" in new_text:
        new_text = new_text.replace("__", "-")
    while "___" in new_text:
        new_text = new_text.replace("___", "-")
    return new_text


def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces_at_beginning():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_consecutive_spaces_at_end():
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_consecutive_spaces_in_middle():
    assert fix_spaces("Example   6  7") == "Example-6_7"

def test_mixed_spaces():
    assert fix_spaces("Example  8  9  10") == "Example-8_9-10"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_multiple_consecutive_spaces():
    assert fix_spaces("Example     11") == "Example-------11"

def test_string_with_tabs():
    assert fix_spaces("Example\t12") == "Example_12"

def test_string_with_newlines():
    assert fix_spaces("Example\n13") == "Example_13"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example \t 14\n") == "Example_14"

def test_long_string_with_consecutive_spaces():
    long_string = "This is a very long string with   multiple    consecutive   spaces."
    expected = "This_is_a_very_long_string_with-multiple-consecutive-spaces."
    assert fix_spaces(long_string) == expected

def test_special_characters():
    assert fix_spaces("!@#$%^ Example &*()") == "_!@#$%^Example_&*()"

def test_numbers_and_spaces():
    assert fix_spaces("123  456 789") == "123-456_789"

def test_unicode_characters():
    assert fix_spaces("你好 世界  ") == "你好_世界-"

def test_long_string_with_many_spaces():
    long_string = "This is a very long string with many spaces.   It has more than two consecutive spaces in several places.  Let's see if it works correctly.     "
    expected_result = "_This_is_a_very_long_string_with_many_spaces.-It_has_more_than_two_consecutive_spaces_in_several_places.-Let's_see_if_it_works_correctly-------"
    assert fix_spaces(long_string) == expected_result