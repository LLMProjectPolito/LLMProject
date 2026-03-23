import pytest
import math


# Focus: Boundary Values
def test_boundary_valid_name_with_max_digits():
    assert file_name_check("a123.txt") == 'Yes'

def test_boundary_valid_name_no_digits():
    assert file_name_check("example.txt") == 'Yes'

def test_boundary_invalid_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

# Focus: Logic Branches
def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

# Focus: Type Scenarios
def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_file_name_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_invalid_file_name_extension():
    assert file_name_check("example.pdf") == 'No'