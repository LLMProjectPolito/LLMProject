import pytest
import math

import pytest

def test_basic():
    assert fix_spaces("Example 1") == "Example_1"

import pytest

def test_edge():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("  a   b  ") == "-a-b-"
    assert fix_spaces("") == ""
    assert fix_spaces("a") == "a"
    assert fix_spaces("a ") == "a_"
    assert fix_spaces(" a ") == "_a_"
    assert fix_spaces("a  b") == "a-b"

import pytest

def test_fix_spaces_many_consecutive_spaces():
    assert fix_spaces("  abc   def  ") == "-abc-def-"