
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
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_whitespace():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  Hello  World  ") == "-Hello-World-"

def test_consecutive_spaces():
    assert fix_spaces("This  is   a    test") == "This-is-a-test"
    assert fix_spaces("   Example") == "-Example"
    assert fix_spaces("Example   ") == "Example-"
    assert fix_spaces("   Test  ") == "-Test-"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with many spaces.   It has  multiple   consecutive   spaces."
    expected_result = "This_is_a_very_long_string_with_many_spaces.-It-has-multiple-consecutive-spaces."
    assert fix_spaces(long_string) == expected_result

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example\t 1 \n 2") == "Example_1_2"

def test_only_whitespace():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("\t\t") == "--"
    assert fix_spaces("\n\n") == "--"

def test_invalid_input():
    with pytest.raises(TypeError):
        fix_spaces(123)
    with pytest.raises(TypeError):
        fix_spaces(["a", "b"])
    with pytest.raises(TypeError):
        fix_spaces(None)
    with pytest.raises(TypeError):
        fix_spaces({})
    with pytest.raises(TypeError):
        fix_spaces(())