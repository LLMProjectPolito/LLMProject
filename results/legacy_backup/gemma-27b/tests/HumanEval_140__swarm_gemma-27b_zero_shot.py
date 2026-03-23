import pytest

def test_leading_and_trailing_spaces_with_multiple_inner_spaces():
    assert fix_spaces("   abc  def   ") == "-abc-def-"