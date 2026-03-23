import pytest
import math


# Focus: Boundary Values
import pytest

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
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

@pytest.mark.parametrize("file_name", [
    "example.txt",  # Valid
    "a.txt",  # Valid
    "A.exe",  # Valid
    "123.dll", # Invalid - starts with digit
    "1example.txt", # Invalid - starts with digit
    "example1.txt", # Valid
    "example12.exe", # Valid
    "example123.dll", # Valid
    "example1234.txt", # Invalid - too many digits
    "ex.txt", # Valid
    "e.exe", # Valid
    "e.dll", # Valid
    ".txt",  # Invalid - empty before dot
    "example.",  # Invalid - empty after dot
    "example.tx",  # Invalid - invalid extension
    "example.exe1", # Invalid - invalid extension
    "example..txt", # Invalid - multiple dots
    "exampletxt", # Invalid - no dot
    "1234.txt", # Invalid - too many digits
    "123example.txt", # Invalid - starts with digit
    "example.TXT", # Invalid - extension case sensitive
])
def test_boundary_values(file_name):
    assert file_name_check(file_name) == pytest.param(
        "Yes", marks=pytest.mark.xfail if file_name in ["123.dll", ".txt", "example.", "example.tx", "example.exe1", "example..txt", "exampletxt", "1234.txt", "123example.txt", "example.TXT"] else None
    ) or pytest.param(
        "No", marks=pytest.mark.xfail if file_name not in ["123.dll", ".txt", "example.", "example.tx", "example.exe1", "example..txt", "exampletxt", "1234.txt", "123example.txt", "example.TXT"] else None
    )

# Focus: Logic Branches
import pytest

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
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

@pytest.mark.parametrize("file_name, expected", [
    ("example.txt", "Yes"),
    ("1example.dll", "No"),
    ("examp1e.txt", "Yes"),
    ("123example.exe", "No"),
    ("example", "No"),
    ("example.", "No"),
    (".txt", "No"),
    ("example.pdf", "No"),
    ("ExAmPlE.tXt", "Yes"),
    ("12example.txt", "No"),
    ("example1.txt", "Yes"),
    ("example12.txt", "Yes"),
    ("example123.txt", "No"),
    ("example.txttxt", "No"),
    ("example..txt", "No"),
    ("example.123", "No"),
])
def test_file_name_check_logic_branches(file_name, expected):
    assert file_name_check(file_name) == expected

# Focus: Invalid Input Handling
import pytest

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
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

@pytest.mark.parametrize("file_name, expected", [
    ("1234example.txt", "No"),  # More than three digits
    ("example..txt", "No"),  # More than one dot
    (".txt", "No"),  # Empty substring before dot
    ("1example.txt", "No"),  # Starts with a digit
    ("example.pdf", "No"),  # Invalid extension
    ("example.txtt", "No"), # Invalid extension
    ("example.t", "No"), # Invalid extension
    ("ExAmPlE.TxT", "Yes"), # Uppercase and lowercase
    ("example.EXE", "Yes"),
    ("example.dll", "Yes"),
    ("example.txt", "Yes"),
    ("a.txt", "Yes"),
    ("A.txt", "Yes"),
    ("1a.txt", "No"),
    ("a1.txt", "Yes"),
    ("a12.txt", "Yes"),
    ("a123.txt", "Yes"),
    ("a1234.txt", "No"),
    ("example.txt.", "No"), #dot at the end
    ("example..txt", "No") #multiple dots
])
def test_invalid_input_handling(file_name, expected):
    assert file_name_check(file_name) == expected