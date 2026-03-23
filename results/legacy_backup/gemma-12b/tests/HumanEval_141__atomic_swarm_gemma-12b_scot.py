import pytest
import math

def test_basic():
    assert file_name_check("example.txt") == 'Yes'

def test_empty_file_name():
    """Test with an empty file name."""
    assert file_name_check("") == "No"

def test_file_name_check_invalid_extension():
    """Test that file names with invalid extensions return 'No'."""
    assert file_name_check("example.invalid") == 'No'