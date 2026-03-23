import pytest
import math


# Focus: Boundary Values
def test_boundary_valid_name_with_max_digits():
    assert file_name_check("a123.txt") == 'Yes'

def test_boundary_valid_name_with_min_digits():
    assert file_name_check("a.txt") == 'Yes'

def test_boundary_valid_name_with_min_prefix():
    assert file_name_check("a.txt") == 'Yes'

def test_boundary_valid_name_with_max_prefix():
    assert file_name_check("abcdef.txt") == 'Yes'

# Focus: Type Scenarios
def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("123example.txt") == 'No'

def test_invalid_file_name_wrong_extension():
    assert file_name_check("example.pdf") == 'No'

# Focus: Logic Branches
def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'