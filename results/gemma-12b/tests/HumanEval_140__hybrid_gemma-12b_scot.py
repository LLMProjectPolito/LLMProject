
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
    i = 0
    while i < len(text):
        if text[i] == ' ':
            if i + 1 < len(text) and text[i+1] == ' ' and i + 2 < len(text) and text[i+2] == ' ':
                result += "-"
                i += 3
            else:
                result += "_"
                i += 1
        else:
            result += text[i]
            i += 1
    return result

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_multiple_spaces(self):
        assert fix_spaces("Example 1 2 3") == "Example_1_2_3"

    def test_consecutive_spaces(self):
        assert fix_spaces("Example   3") == "Example-3"

    def test_consecutive_spaces_less_than_three(self):
        assert fix_spaces("Example  1") == "Example__1"

    def test_leading_spaces(self):
        assert fix_spaces(" Example 1") == "_Example_1"

    def test_trailing_spaces(self):
        assert fix_spaces("Example 1 ") == "Example_1_"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces(" Example 2 ") == "_Example_2_"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2 3") == "Example__1-2_3"

    def test_string_with_numbers(self):
        assert fix_spaces("1 2 3") == "_1_2_3"

    def test_string_with_special_characters(self):
        assert fix_spaces("Example!@#$%^&*() 1") == "Example!@#$%^&*()_1"