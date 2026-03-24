
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
import math


# Focus: Boundary Values
import pytest

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_exactly_two_consecutive_spaces():
    assert fix_spaces("Example  3") == "Example__3"

def test_fix_spaces_many_spaces_at_beginning():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_fix_spaces_many_spaces_at_end():
    assert fix_spaces("Example 4   ") == "Example_4-"

# Focus: Consecutive Spaces
import pytest

def test_consecutive_spaces_none():
    assert fix_spaces("Example") == "Example"

def test_consecutive_spaces_one():
    assert fix_spaces("Example 1") == "Example_1"

def test_consecutive_spaces_two():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_consecutive_spaces_three():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces_more_than_three():
    assert fix_spaces("Example    4") == "Example-4"

def test_consecutive_spaces_start_and_end():
    assert fix_spaces("  Example   5  ") == "-Example-5-"

def test_consecutive_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_consecutive_spaces_mixed():
    assert fix_spaces("  a  b   c d    e") == "-a-b-c d-e"

# Focus: Leading/Trailing Spaces
import pytest

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_leading_trailing_and_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_no_leading_trailing_spaces():
    assert fix_spaces("Example 1") == "Example_1"