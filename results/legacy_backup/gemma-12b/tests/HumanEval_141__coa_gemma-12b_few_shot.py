import pytest
import math


# Focus: Boundary Values
import re

def test_file_name_check_max_digits_boundary():
    assert file_name_check("a123.txt") == 'No'
    assert file_name_check("a12.txt") == 'Yes'
    assert file_name_check("a1.txt") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("a0.txt") == 'Yes'
    assert file_name_check("a00.txt") == 'Yes'
    assert file_name_check("a000.txt") == 'No'

def test_file_name_check_dot_boundary():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("example.") == 'No'
    assert file_name_check("example..txt") == 'No'

def test_file_name_check_extension_boundary():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.exe") == 'Yes'
    assert file_name_check("example.dll") == 'Yes'
    assert file_name_check("example.abc") == 'No'
    assert file_name_check("example.t") == 'No'
    assert file_name_check("example.tx") == 'No'

# Focus: Logic Branches
import re

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("abc.exe") == "Yes"
    assert file_name_check("longname.dll") == "Yes"

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234.txt") == "No"
    assert file_name_check("123.txt") == "Yes"

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example.txt.extra") == "No"
    assert file_name_check("example") == "No"

def test_file_name_check_invalid_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check(".txt") == "No"

def test_file_name_check_invalid_suffix():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.t") == "No"

# Focus: Type Scenarios
def test_file_name_check_valid():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("abc.exe") == 'Yes'
    assert file_name_check("long_name.dll") == 'Yes'

def test_file_name_check_invalid_digit_count():
    assert file_name_check("1234.txt") == 'No'
    assert file_name_check("123.txt") == 'Yes'

def test_file_name_check_invalid_dot_count():
    assert file_name_check("example.txt.extra") == 'No'
    assert file_name_check("example") == 'No'