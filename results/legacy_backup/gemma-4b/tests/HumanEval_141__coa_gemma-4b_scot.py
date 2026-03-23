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
    if len(file_name) > 20:
        return 'No'
    if file_name.count('0' <= char <= '9') > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    parts = file_name.split('.')
    if not parts[0]:
        return 'No'
    if not 'a' <= parts[0][0] <= 'z' and not 'A' <= parts[0][0] <= 'Z':
        return 'No'
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested thoroughly, focusing on boundary values for the number of digits, the presence of a single dot, the starting character of the substring before the dot, and the allowed extensions.
### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_name: Tests a valid file name.
### - test_too_many_digits: Tests a file name with more than three digits.
### - test_no_dot: Tests a file name without a dot.
### - test_invalid_start_char: Tests a file name starting with a digit.
### - test_invalid_extension: Tests a file name with an invalid extension.
### STEP 3: CODE - Write the high-quality pytest suite.

### STEP 3: CODE - Write the high-quality pytest suite.
def test_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_too_many_digits():
    assert file_name_check("1example.dll") == 'No'

def test_no_dot():
    assert file_name_check("exampledll") == 'No'

def test_invalid_start_char():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

# Focus: Type Scenarios
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
    if not file_name:
        return 'No'

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not 'a' <= prefix[0] <= 'z' or not 'A' <= prefix[0] <= 'Z':
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The test functions should focus solely on the 'Type Scenarios' dimension,
# meaning they should test different types of input file names to ensure the
# function handles them correctly according to the specified rules.
# We need to cover cases with valid and invalid digits, multiple dots,
# invalid prefixes, and invalid suffixes.

# STEP 2: PLAN - List test functions names and scenarios.
# test_valid_name: Tests a valid file name.
# test_invalid_digits: Tests a file name with more than three digits.
# test_multiple_dots: Tests a file name with more than one dot.
# test_invalid_prefix: Tests a file name with an invalid prefix.
# test_invalid_suffix: Tests a file name with an invalid suffix.
# test_empty_name: Tests an empty file name.

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_valid_name():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_digits():
    assert file_name_check("1example.dll") == 'No'

def test_multiple_dots():
    assert file_name_check("example..txt") == 'No'

def test_invalid_prefix():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_empty_name():
    assert file_name_check("") == 'No'

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
    if not file_name:
        return 'No'

    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    dot_index = file_name.find('.')
    prefix = file_name[:dot_index]
    suffix = file_name[dot_index + 1:]

    if not prefix or not prefix[0].isalpha():
        return 'No'

    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested to ensure it correctly validates file names based on specific criteria:
### - Maximum number of digits
### - Presence of exactly one dot
### - Prefix starts with a letter
### - Suffix is one of the allowed extensions

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_name: Tests a valid file name.
### - test_too_many_digits: Tests a file name with more than three digits.
### - test_invalid_prefix: Tests a file name with an invalid prefix (not starting with a letter).
### - test_invalid_suffix: Tests a file name with an invalid suffix.
### - test_no_dot: Tests a file name without a dot.

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested to ensure it correctly validates file names based on specific criteria:
### - Maximum number of digits
### - Presence of exactly one dot
### - Prefix starts with a letter
### - Suffix is one of the allowed extensions

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_name: Tests a valid file name.
### - test_too_many_digits: Tests a file name with more than three digits.
### - test_invalid_prefix: Tests a file name with an invalid prefix (not starting with a letter).
### - test_invalid_suffix: Tests a file name with an invalid suffix.
### - test_no_dot: Tests a file name without a dot.

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested to ensure it correctly validates file names based on specific criteria:
### - Maximum number of digits
### - Presence of exactly one dot
### - Prefix starts with a letter
### - Suffix is one of the allowed extensions

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_name: Tests a valid file name.
### - test_too_many_digits: Tests a file name with more than three digits.
### - test_invalid_prefix: Tests a file name with an invalid prefix (not starting with a letter).
### - test_invalid_suffix: Tests a file name with an invalid suffix.
### - test_no_dot: Tests a file name without a dot.

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `file_name_check` needs to be tested to ensure it correctly validates file names based on specific criteria:
### - Maximum number of digits
### - Presence of exactly one dot
### - Prefix starts with a letter
### - Suffix is one of the allowed extensions

### STEP 2: PLAN - List test functions names and scenarios.
### Test functions:
### - test_valid_name: Tests a valid file name.
### - test_too_many_digits: Tests a file name with more than three digits.
### - test_invalid_prefix: Tests a file name with an invalid prefix (not starting with a letter).
### - test_invalid_suffix: Tests a file name with an invalid suffix.
### - test_no_dot: Tests a file name without a dot.

### STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("file_name, expected", [
    ("example.txt", "Yes"),
    ("1example.dll", "No"),
    ("example123.txt", "No"),
    ("1example.exe", "No"),
    ("example.123", "No"),
    ("example.abc", "Yes"),
    ("example.txt.bak", "No"),
    ("example.txt", "Yes"),
    ("example.dll", "Yes"),
    ("example.exe", "Yes"),
    ("", "No"),
    ("123.txt", "No"),
    ("a123.txt", "Yes"),
    ("a.txt", "Yes"),
    ("a.b.txt", "No"),
])
def test_valid_name(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name, expected", [
    ("1example.dll", "No"),
    ("example123.txt", "No"),
    ("example.exe", "No"),
    ("example.123", "No"),
    ("123.txt", "No"),
])
def test_too_many_digits(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name, expected", [
    ("1example.dll", "No"),
    ("example123.txt", "No"),
])
def test_invalid_prefix(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name, expected", [
    ("example.123", "No"),
    ("example.abcd", "No"),
])
def test_invalid_suffix(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize("file_name, expected", [
    ("example", "No"),
    ("example.txt.bak", "No"),
])
def test_no_dot(file_name, expected):
    assert file_name_check(file_name) == expected