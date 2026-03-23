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
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    before_dot = parts[0]
    after_dot = parts[1]

    if not before_dot:
        return 'No'

    if not before_dot[0].isalpha():
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Pytest tests
def test_valid_filenames():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'
    assert file_name_check("file123.txt") == 'Yes'

def test_invalid_filenames():
    assert file_name_check("1example.dll") == 'No'  # Starts with a digit
    assert file_name_check("example") == 'No'  # No dot
    assert file_name_check("example.pdf") == 'No'  # Invalid extension
    assert file_name_check(".txt") == 'No'  # Empty before dot
    assert file_name_check("example..txt") == 'No'  # Multiple dots
    assert file_name_check("example1234.txt") == 'No'  # Too many digits
    assert file_name_check("123example.txt") == 'No' #Too many digits and starts with digit
    assert file_name_check("example.tXt") == 'No' #Extension case sensitive
    assert file_name_check("example.txt.") == 'No' #Empty after dot
    assert file_name_check("example. ") == 'No' #Space after dot
    assert file_name_check("!example.txt") == 'No' #Starts with special character
    assert file_name_check("example.txt1") == 'No' #Extension is not valid
    assert file_name_check("example.123") == 'No' #Extension is not valid
    assert file_name_check("example.txttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxttxttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxttxttxttxttxt") == 'No' #Extension is not valid
    assert file_name_check("example.txttxttxttxttxttxttxttxttxt") == 'No' #Extension is not valid