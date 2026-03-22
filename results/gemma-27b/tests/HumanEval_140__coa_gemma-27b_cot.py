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

def test_fix_spaces_more_than_three_consecutive_spaces():
    assert fix_spaces("Example    4") == "Example-4"

def test_fix_spaces_mix_of_single_and_multiple_spaces():
    assert fix_spaces("Example  1 2   3") == "Example-1_2-3"

# Focus: Consecutive Spaces
import pytest

def test_consecutive_spaces_none():
    assert fix_spaces("Example") == "Example"

def test_consecutive_spaces_single():
    assert fix_spaces("Example 1") == "Example_1"

def test_consecutive_spaces_leading():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_consecutive_spaces_multiple():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_consecutive_spaces_only():
    assert fix_spaces("   ") == "-"

def test_consecutive_spaces_mixed():
    assert fix_spaces("  a  b   c") == "_a_b-c"

def test_consecutive_spaces_start_end():
    assert fix_spaces("  abc  ") == "_abc_"

def test_consecutive_spaces_empty_string():
    assert fix_spaces("") == ""

# Focus: Leading/Trailing Spaces
import pytest

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_trailing_single_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_leading_trailing_multiple_spaces():
    assert fix_spaces("  Example   3  ") == "__Example-3__"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example   Test") == "Example-Test"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  a b  c   d ") == "__a_b__c-d__"