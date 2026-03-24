
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

import pytest
import math


# Focus: Boundary Values
import pytest

def test_file_name_check_valid_1():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_valid_2():
    assert file_name_check("data.dll") == "Yes"

def test_file_name_check_invalid_1():
    assert file_name_check("1example.dll") == "No"

def test_file_name_check_invalid_2():
    assert file_name_check("123.txt") == "No"

def test_file_name_check_invalid_3():
    assert file_name_check("example..txt") == "No"

def test_file_name_check_invalid_4():
    assert file_name_check("example.exe") == "No"

def test_file_name_check_invalid_5():
    assert file_name_check("example.pdf") == "No"

# Focus: Type Scenarios
import pytest

def test_type_scenario_1():
    assert file_name_check("example.txt") == "Yes"

def test_type_scenario_2():
    assert file_name_check("1example.dll") == "No"

def test_type_scenario_3():
    assert file_name_check("example.exe") == "Yes"

def test_type_scenario_4():
    assert file_name_check("example..txt") == "No"

def test_type_scenario_5():
    assert file_name_check("example.abc") == "No"

def test_type_scenario_6():
    assert file_name_check("example.txt.txt") == "No"

# Focus: Logic Branches
import pytest

def test_valid_file_name_one_dot():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("data.dll") == 'Yes'
    assert file_name_check("report.exe") == 'Yes'

def test_invalid_file_name_no_dot():
    assert file_name_check("example123") == 'No'
    assert file_name_check("1example") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example..txt") == 'No'
    assert file_name_check("example.txt.bak") == 'No'

def test_invalid_file_name_digit_count():
    assert file_name_check("123example.txt") == 'No'
    assert file_name_check("example123.txt") == 'No'
    assert file_name_check("example1234.txt") == 'No'

def test_invalid_file_name_prefix():
    assert file_name_check("1example.txt") == 'No'
    assert file_name_check("0example.txt") == 'No'
    assert file_name_check("2example.txt") == 'No'

def test_invalid_file_name_suffix():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'
    assert file_name_check("example.123") == 'No'