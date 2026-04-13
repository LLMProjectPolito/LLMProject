
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

def test_file_name_valid():
    """Tests cases that should return 'Yes'"""
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("document.exe") == 'Yes'
    assert file_name_check("library.dll") == 'Yes'
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("File123.txt") == 'Yes'
    assert file_name_check("MyFile1.exe") == 'Yes'
    assert file_name_check("Test_12.dll") == 'Yes'

def test_file_name_digit_limit():
    """Tests the rule: no more than three digits"""
    assert file_name_check("file1234.txt") == 'No'
    assert file_name_check("1234a.exe") == 'No'
    assert file_name_check("a1b2c3d4.dll") == 'No'

def test_file_name_dot_count():
    """Tests the rule: exactly one dot"""
    assert file_name_check("exampletxt") == 'No'  # No dot
    assert file_name_check("example.test.txt") == 'No'  # Too many dots
    assert file_name_check("example..txt") == 'No'  # Too many dots

def test_file_name_prefix():
    """Tests the rule: prefix not empty and starts with a latin letter"""
    assert file_name_check(".txt") == 'No'  # Empty prefix
    assert file_name_check("1example.dll") == 'No'  # Starts with digit
    assert file_name_check("_example.txt") == 'No'  # Starts with special char
    assert file_name_check(" example.exe") == 'No'  # Starts with space

def test_file_name_extension():
    """Tests the rule: extension must be 'txt', 'exe', or 'dll'"""
    assert file_name_check("example.pdf") == 'No'  # Invalid extension
    assert file_name_check("example.png") == 'No'  # Invalid extension
    assert file_name_check("example.") == 'No'  # Empty extension
    assert file_name_check("example.TXT") == 'No'  # Case sensitivity check
    assert file_name_check("example.exee") == 'No' # Partial match check