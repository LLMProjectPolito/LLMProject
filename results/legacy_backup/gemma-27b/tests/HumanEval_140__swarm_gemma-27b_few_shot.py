import pytest

def test_fix_spaces_many_consecutive():
    assert fix_spaces("  abc   def  ") == "-abc-def-"

def test_fix_spaces_single_space():
    assert fix_spaces(" a b ") == "-a-b-"

def test_fix_spaces_leading_and_trailing():
    assert fix_spaces("  a   b  ") == "-a-b-"

def test_fix_spaces_no_spaces():
    assert fix_spaces("abc") == "-abc-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == "-"