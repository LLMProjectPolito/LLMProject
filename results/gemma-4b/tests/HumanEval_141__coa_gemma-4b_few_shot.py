import pytest
import math


# Focus: Boundary Values
def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("test.dll") == "Yes"
    assert file_name_check("a.exe") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("123.txt") == "No"
    assert file_name_check("abc123.txt") == "No"

def test_file_name_check_invalid_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("example..txt") == "No"

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("abc1example.txt") == "No"

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"

# Focus: Type Scenarios
def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("1example.txt") == "No"

def test_file_name_check_invalid_dot():
    assert file_name_check("example.") == "No"

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == "No"

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == "No"

# Focus: Logic Branches
def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("test.dll") == "Yes"
    assert file_name_check("a.exe") == "Yes"

def test_file_name_check_invalid_digits():
    assert file_name_check("123.txt") == "No"
    assert file_name_check("abc123.txt") == "No"

def test_file_name_check_invalid_dot():
    assert file_name_check("abc.txt.txt") == "No"
    assert file_name_check("abc.") == "No"

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("a1example.txt") == "No"

def test_file_name_check_invalid_suffix():
    assert file_name_check("abc.pdf") == "No"
    assert file_name_check("abc.jpg") == "No"