
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
from typing import List

def fix_spaces(text: str) -> str:
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
    spaces = 0
    for char in text:
        if char == ' ':
            spaces += 1
            if spaces > 2:
                result += '-'
            else:
                result += '_'
        else:
            result += char
            spaces = 0
    return result

class TestFixSpaces:
    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_multiple_consecutive_spaces_at_start(self):
        assert fix_spaces("   Example 4") == "-Example_4"

    def test_multiple_consecutive_spaces_at_end(self):
        assert fix_spaces("Example 5   ") == "Example_5-"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1  2   3") == "Example__1_2-3"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_long_string_with_consecutive_spaces(self):
        assert fix_spaces("This is a  long   string with  multiple   spaces.") == "This_is_a-long-string_with_multiple-spaces."

    def test_string_with_tabs_and_spaces(self):
        assert fix_spaces("Example\t 1") == "Example_1"

    def test_string_with_newline_and_spaces(self):
        assert fix_spaces("Example\n 1") == "Example_1"