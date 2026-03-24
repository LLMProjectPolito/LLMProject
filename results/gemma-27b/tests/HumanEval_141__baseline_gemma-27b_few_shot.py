
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

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A123.txt") == 'Yes'
    assert file_name_check("file.txt") == 'Yes'

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.backup") == 'No'

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("example.jpg") == 'No'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'
    assert file_name_check("a1234.exe") == 'No'

def test_invalid_file_name_digit_before_dot():
    assert file_name_check("1a.txt") == 'No'

def test_empty_string():
    assert file_name_check("") == 'No'