
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
import re

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
    new_text = re.sub(r"{3,}", "-", new_text)
    return new_text

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_space(self):
        assert fix_spaces("Example 3 ") == "Example_3_"

    def test_consecutive_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_consecutive_spaces_start(self):
        assert fix_spaces("  Example 4") == "-Example_4"

    def test_consecutive_spaces_end(self):
        assert fix_spaces("Example 5  ") == "Example_5-"

    def test_consecutive_spaces_middle(self):
        assert fix_spaces("Example   6  ") == "Example-6-"

    def test_many_consecutive_spaces(self):
        assert fix_spaces("Example     7") == "Example--------7"

    def test_mixed_spaces(self):
        assert fix_spaces(" Example  8  ") == "_Example-8-"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_many_consecutive_spaces_more_than_3(self):
        assert fix_spaces("Example  EEEE  ") == "Example--------EEEE-"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces("  Example 9  ") == "-Example_9-"

    def test_consecutive_spaces_greater_than_3(self):
        assert fix_spaces("Example      10") == "Example----------10"