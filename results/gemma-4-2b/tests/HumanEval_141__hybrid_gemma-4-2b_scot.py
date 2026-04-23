
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

```python
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
    dot_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
        if char == '.':
            dot_count += 1

    if digit_count > 3 or dot_count != 1:
        return 'No'

    parts = file_name.split('.')
    if not parts[0]:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'
    
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("1example.dll", "No"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example", "No"),
        ("example..txt", "No"),
        ("example", "No"),
        ("123example.txt", "No"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("", "No"),
        ("....txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.dll", "Yes"),
        ("a.123", "No"),
        ("a.txt", "Yes"),
        ("a.exe", "Yes"),
        ("a.dll", "Yes"),
    ],
)
def test_valid_file_name_1(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("1example.exe", "No"),
        ("1example.dll", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_valid_file_name_2(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_valid_file_name_3(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("123example.txt", "No"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_1(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example..txt", "No"),
        ("example.txt", "Yes"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_2(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_3(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("123example.txt", "No"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_4(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_5(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("", "No"),
        ("....txt", "No"),
        ("a.txt", "Yes"),
        ("A.exe", "Yes"),
        ("a.dll", "Yes"),
        ("a.123", "No"),
    ],
)
def test_invalid_file_name_6(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_valid_file_name_7(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_8(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_9(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_invalid_file_name_10(file_name, expected):
    assert file_name_check(file_name) == expected

@pytest.mark.parametrize(
    "file_name, expected",
    [
        ("example.txt", "Yes"),
        ("example.exe", "Yes"),
        ("example.dll", "Yes"),
        ("example1.txt", "No"),
        ("example.xyz", "No"),
        ("example", "No"),
        ("example.txt", "Yes"),
    ],
)
def test_valid_file_name_11(file_name, expected):