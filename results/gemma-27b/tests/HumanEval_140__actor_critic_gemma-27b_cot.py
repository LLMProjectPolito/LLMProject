
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

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example 2 ") == "_Example_2_"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_multiple_spaces_mixed():
    assert fix_spaces("  Example   4  ") == "_Example-4_"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_string_with_multiple_spaces():
    assert fix_spaces("This is a long string with   multiple spaces.") == "This_is_a_long_string_with-multiple_spaces."

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example \t\n 1") == "_Example_-1"

def test_consecutive_whitespace():
    assert fix_spaces("abc\t\t\n\n def") == "abc---def"

def test_spaces_adjacent_to_punctuation():
    assert fix_spaces("Example, 1") == "Example,_1"
    assert fix_spaces("1. Example") == "1._Example"

def test_invalid_input():
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_multiple_consecutive_tabs():
    assert fix_spaces("abc\t\t\tdef") == "abc---def"

def test_multiple_consecutive_newlines():
    assert fix_spaces("abc\n\n\ndef") == "abc---def"

def test_mixed_consecutive_whitespace():
    assert fix_spaces("abc \t\n\t\n def") == "abc---def"