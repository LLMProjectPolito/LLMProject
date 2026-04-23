
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

def test_basic():
    assert fix_spaces("Example 1") == "Example_1"

def test_edge():
    assert fix_spaces("   ") == "-"

def test_more_than_two_consecutive_spaces():
    assert fix_spaces("  abc   def  ") == "-abc-def-"