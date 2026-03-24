
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
    new_text = ""
    i = 0
    while i < len(text):
        if text[i] == " ":
            if i + 1 < len(text) and text[i+1] == " " and i + 2 < len(text) and text[i+2] == " ":
                new_text += "-"
                i += 3
            else:
                new_text += "_"
                i += 1
        else:
            new_text += text[i]
            i += 1
    return new_text

class TestFixSpaces:
    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_multiple_spaces(self):
        assert fix_spaces("Example 1 2") == "Example_1_2"

    def test_leading_spaces(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_spaces(self):
        assert fix_spaces("Example 2 ") == "Example_2_"

    def test_mixed_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_consecutive_spaces(self):
        assert fix_spaces("Example   1") == "Example-1"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_string_with_other_characters(self):
        assert fix_spaces("Example! 1?") == "Example!_1?"

    def test_string_with_only_spaces(self):
        assert fix_spaces("   ") == "-"