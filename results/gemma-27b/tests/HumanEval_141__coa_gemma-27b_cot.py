import pytest
import math


# Focus: Boundary Values
import pytest

def test_file_name_check_boundary_digit_count():
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("a1234.txt") == "No"
    assert file_name_check("123a.txt") == "No"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("a1.txt") == "Yes"

def test_file_name_check_boundary_dot_count():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check(".txt") == "No"

def test_file_name_check_boundary_extension():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.doc") == "No"
    assert file_name_check("example.TXT") == "No"

# Focus: Logic Branches
import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("AnotherExample.exe") == "Yes"
    assert file_name_check("file123.dll") == "Yes"
    assert file_name_check("A.txt") == "Yes"

def test_invalid_file_name_digit_count():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.dll") == "No"
    assert file_name_check("123example123.exe") == "No"

def test_invalid_file_name_dot_count():
    assert file_name_check("example.txt.exe") == "No"
    assert file_name_check("example..txt") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2AnotherExample.exe") == "No"
    assert file_name_check("!file.dll") == "No"

def test_invalid_file_name_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("AnotherExample.jpg") == "No"
    assert file_name_check("file123.zip") == "No"

def test_invalid_file_name_empty_prefix():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

# Focus: Invalid Input Handling
import pytest

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