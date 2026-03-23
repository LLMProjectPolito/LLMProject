import pytest

def test_fix_spaces_with_leading_and_trailing_spaces_and_multiple_consecutive_spaces():
    """Test case for leading/trailing spaces and multiple consecutive spaces."""
    assert fix_spaces("   abc  def   ") == "---abc-def---"