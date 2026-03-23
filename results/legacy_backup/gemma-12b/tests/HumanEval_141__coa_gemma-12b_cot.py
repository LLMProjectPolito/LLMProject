import pytest
import math


# Focus: Boundary Values
def test_file_name_check_boundary_digit_limit():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("a1.txt") == 'Yes'
    assert file_name_check("a12.txt") == 'Yes'
    assert file_name_check("a123.txt") == 'Yes'
    assert file_name_check("a1234.txt") == 'No'

def test_file_name_check_boundary_dot_count():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("a..txt") == 'No'
    assert file_name_check("atxt") == 'No'
    assert file_name_check(".txt") == 'No'

def test_file_name_check_boundary_substrings():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("a.") == 'No'
    assert file_name_check("1.txt") == 'No'

# Focus: Logic Branches
import pytest

def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == "No"

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == "No"

# Focus: Type Scenarios
def test_file_name_check_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'

def test_file_name_check_invalid_extension():
    assert file_name_check("example.pdf") == 'No'