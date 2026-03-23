import pytest
import math

def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_all_digits():
    assert file_name_check("123.txt") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'