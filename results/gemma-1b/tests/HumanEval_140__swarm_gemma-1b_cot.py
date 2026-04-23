
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

def fix_spaces(text):
    """
    Fixes spaces in a string, ensuring only valid code is output.
    """
    if text is None:
        return ""
    
    if text.strip() == "":
        return ""
    
    return text

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one_one"
    assert fix_spaces("  one  one  ") == "_one_one_long"
    assert fix_spaces("  one  one  one") == "_one_one_long_long"
    print("Test case passed")

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  one") == "_one"
    assert fix_spaces("  one  ") == "_one"
    assert fix_spaces("  one  one") == "_one_one"
    assert fix_spaces("  one  one  ") == "_one_one_long"
    assert fix_spaces("  one  one  one") == "_one_one_long_long"
    print("Test case passed")