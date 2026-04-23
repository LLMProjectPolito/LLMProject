
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

    def test_multiple_single_spaces(self):
        assert fix_spaces("Example 1 2") == "Example_1_2"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_leading_spaces(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_spaces(self):
        assert fix_spaces("Example 2 ") == "Example_2_"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces(" Example 2 ") == "_Example_2_"

    def test_consecutive_spaces_less_than_three(self):
        assert fix_spaces("Example  1") == "Example__1"

    def test_consecutive_spaces_more_than_two(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_multiple_consecutive_blocks(self):
        assert fix_spaces(" Example   3   4") == "_Example-3_4"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2  3") == "Example-1_2_3"

    def test_two_consecutive_spaces(self):
        assert fix_spaces("Example  1") == "Example__1"

    def test_multiple_hyphens(self):
        assert fix_spaces("   ") == "-"

    def test_mixed_spaces_2(self):
        assert fix_spaces("a  b   c") == "a-b_c"