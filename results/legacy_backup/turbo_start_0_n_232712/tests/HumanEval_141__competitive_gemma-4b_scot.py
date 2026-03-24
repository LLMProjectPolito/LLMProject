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
    digits = 0
    dot_count = 0
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    before_dot = parts[0]
    after_dot = parts[1]
    
    for char in before_dot:
        if char.isdigit():
            digits += 1
    
    dot_count = before_dot.count('.')
    
    if digits > 3 or dot_count != 1:
        return 'No'
    
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_file_name_with_digits():
    assert file_name_check("example123.txt") == 'Yes'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example..txt") == 'No'

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_name_digit_start():
    assert file_name_check("1example.txt") == 'No'

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == 'No'

def test_valid_file_name_with_uppercase():
    assert file_name_check("Example.TXT") == 'Yes'

def test_valid_file_name_with_mixed_case():
    assert file_name_check("ExAmPle.txt") == 'Yes'

def test_valid_file_name_with_numbers_and_letters():
    assert file_name_check("example123.txt") == 'Yes'

def test_valid_file_name_with_numbers_and_letters_and_uppercase():
    assert file_name_check("ExAmPle123.TXT") == 'Yes'