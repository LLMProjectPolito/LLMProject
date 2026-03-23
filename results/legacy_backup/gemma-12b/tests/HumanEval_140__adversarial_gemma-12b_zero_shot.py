import pytest
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_multiple_consecutive_spaces_at_start():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_multiple_consecutive_spaces_at_end():
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_mixed_spaces():
    assert fix_spaces("Example  6  7") == "Example__6-7"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_string_with_multiple_consecutive_spaces():
    assert fix_spaces("This is a  very   long string with    multiple     consecutive spaces.") == "This_is_a-very--long_string_with---multiple-----consecutive_spaces."

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example\t 2 \n 3") == "Example_2\n_3"

def test_string_with_consecutive_spaces_and_other_chars():
    assert fix_spaces("Example   abc def   ") == "Example-abc_def-"