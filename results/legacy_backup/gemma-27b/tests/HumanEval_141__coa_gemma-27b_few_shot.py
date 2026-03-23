import pytest
import math


# Focus: Boundary Values
def test_file_name_check_boundary_digits():
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("123.txt") == "No"
    assert file_name_check("a.txt") == "Yes"

def test_file_name_check_boundary_dot():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check(".txt") == "No"

def test_file_name_check_boundary_extension():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.py") == "No"

# Focus: Logic Branches
def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("a12.dll") == 'Yes'
    assert file_name_check("Xyz123.txt") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("example1234.txt") == 'No'

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example.txt.exe") == 'No'
    assert file_name_check("exampletxt") == 'No'

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("!example.txt") == 'No'

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'

def test_file_name_check_empty_prefix():
    assert file_name_check(".txt") == 'No'

# Focus: Invalid Input Handling
def test_invalid_input_too_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_invalid_input_no_dot():
    assert file_name_check("exampletxt") == "No"

def test_invalid_input_multiple_dots():
    assert file_name_check("example.txt.txt") == "No"

def test_invalid_input_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_input_starts_with_digit():
    assert file_name_check("1example.txt") == "No"

def test_invalid_input_invalid_extension():
    assert file_name_check("example.pdf") == "No"