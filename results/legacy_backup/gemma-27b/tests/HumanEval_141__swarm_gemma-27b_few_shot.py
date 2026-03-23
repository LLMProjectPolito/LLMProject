import pytest

def test_filename_check_many_digits():
    assert file_name_check("1234example.txt") == "No"