import pytest

def test_file_name_check_leading_digits():
    """Test case: File name starts with digits, should return 'No'."""
    assert file_name_check("123.txt") == "No"