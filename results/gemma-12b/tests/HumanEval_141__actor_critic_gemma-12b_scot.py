
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
from your_module import file_name_check  # Replace your_module

def test_valid_txt_file():
    assert file_name_check("example.txt") == 'Yes'

def test_valid_exe_file():
    assert file_name_check("example.exe") == 'Yes'

def test_valid_dll_file():
    assert file_name_check("example.dll") == 'Yes'

def test_invalid_extension_pdf():
    assert file_name_check("example.pdf") == 'No'

def test_invalid_extension_doc():
    assert file_name_check("example.doc") == 'No'

def test_invalid_extension_jpg():
    assert file_name_check("example.jpg") == 'No'

def test_invalid_extension_py():
    assert file_name_check("example.py") == 'No'

def test_invalid_extension_java():
    assert file_name_check("example.java") == 'No'

def test_invalid_extension_html():
    assert file_name_check("example.html") == 'No'

def test_invalid_extension_csv():
    assert file_name_check("example.csv") == 'No'

def test_extension_case_insensitive():
    assert file_name_check("example.TXT") == 'Yes'
    assert file_name_check("example.tXt") == 'Yes'
    assert file_name_check("example.TxT") == 'Yes'

def test_leading_whitespace():
    assert file_name_check(" example.txt") == 'No'

def test_trailing_whitespace():
    assert file_name_check("example.txt ") == 'No'

def test_whitespace_within_filename():
    assert file_name_check("example file.txt") == 'No'

def test_dot_at_end():
    assert file_name_check("example.") == 'No'

def test_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_multiple_dots():
    assert file_name_check("example.sub.txt") == 'No'

def test_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_non_letter_start():
    assert file_name_check("1example.txt") == 'No'

def test_empty_string():
    assert file_name_check("") == 'No'

def test_digits_and_letters():
    assert file_name_check("a1b2c.txt") == 'Yes'

def test_special_characters_filename():
    assert file_name_check("example!.txt") == 'No'

def test_special_characters_extension():
    assert file_name_check("example.t!xt") == 'No'

def test_too_many_digits_four():
    assert file_name_check("1234example.txt") == 'No'

def test_too_many_digits_five():
    assert file_name_check("12345example.txt") == 'No'

def test_valid_digits_three():
    assert file_name_check("123example.txt") == 'Yes'

def test_dot_in_middle():
    assert file_name_check("example.a.txt") == 'No'

def test_long_name_within_limit():
    long_name = "a" * 160 + ".txt"
    assert file_name_check(long_name) == 'Yes'

def test_long_name_exceeds_limit():
    long_name = "a" * 170 + ".txt"
    assert file_name_check(long_name) == 'No'