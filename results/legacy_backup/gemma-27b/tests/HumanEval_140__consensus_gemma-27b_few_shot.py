import pytest

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 3 ") == "Example_3_"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces(" Example 3 ") == "_Example_3_"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example  1  2") == "Example-1-2"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   1 2  ") == "-Example-1_2-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_tab_and_space():
    assert fix_spaces("Example\t1") == "Example_1"

def test_fix_spaces_newline_and_space():
    assert fix_spaces("Example\n1") == "Example_1"

def test_fix_spaces_carriage_return_and_space():
    assert fix_spaces("Example\r1") == "Example_1"