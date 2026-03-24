import pytest
from your_module import file_name_check  # Replace your_module

def test_valid_filename():
    assert file_name_check("example.txt") == True
    assert file_name_check("document.dll") == True
    assert file_name_check("my_file.exe") == True
    assert file_name_check("a.txt") == True
    assert file_name_check("A.TXT") == True
    assert file_name_check("longname.txt") == True
    assert file_name_check("valid.exe") == True
    assert file_name_check("another.dll") == True

def test_invalid_filename_too_many_digits():
    assert file_name_check("123example.txt") == False
    assert file_name_check("1234example.txt") == False
    assert file_name_check("12345example.txt") == False
    assert file_name_check("12example.txt") == True
    assert file_name_check("1eexample.txt") == True

def test_invalid_filename_no_dot():
    assert file_name_check("example") == False
    assert file_name_check("exampletxt") == False

def test_invalid_filename_multiple_dots():
    assert file_name_check("example.txt.dll") == False
    assert file_name_check("example..txt") == False

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == False
    assert file_name_check(".exe") == False
    assert file_name_check(".dll") == False

def test_invalid_filename_non_letter_before_dot():
    assert file_name_check("1.txt") == False
    assert file_name_check("_example.txt") == False
    assert file_name_check("!.txt") == False

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.pdf") == False
    assert file_name_check("example.jpg") == False
    assert file_name_check("example.dat") == False
    assert file_name_check("example.") == False
    assert file_name_check("example.invalid") == False

def test_valid_filename_allowed_extensions():
    assert file_name_check("example.txt") == True
    assert file_name_check("document.dll") == True
    assert file_name_check("my_file.exe") == True

def test_filename_with_digits_and_letters():
    assert file_name_check("ex1ample.txt") == True
    assert file_name_check("ex2ample.exe") == True
    assert file_name_check("ex3ample.dll") == True
    assert file_name_check("ex4ample.txt") == False

def test_filename_with_special_characters():
    assert file_name_check("example!.txt") == False
    assert file_name_check("example#.txt") == False
    assert file_name_check("example$.txt") == False
    assert file_name_check("example!.exe") == False
    assert file_name_check("example#.dll") == False
    assert file_name_check("example@.txt") == False

def test_empty_filename():
    assert file_name_check("") == False

def test_filename_with_whitespace():
    assert file_name_check(" example.txt") == False
    assert file_name_check("example.txt ") == False
    assert file_name_check(" example.txt ") == False

def test_long_filename():
    long_name = "a" * 100 + ".txt"
    assert file_name_check(long_name) == True

    very_long_name = "a" * 200 + ".txt"
    assert file_name_check(very_long_name) == False

def test_filename_with_path():
    assert file_name_check("/example.txt") == False
    assert file_name_check("example.txt/") == False
    assert file_name_check("path/to/example.txt") == False
    assert file_name_check("path\\to\\example.txt") == False

def test_unicode_filename():
    assert file_name_check("你好.txt") == False  # Assuming the function doesn't support Unicode
    assert file_name_check("example.你好") == False

def test_filename_with_dot():
    assert file_name_check(".") == False

def test_filename_with_extension_only():
    assert file_name_check(".txt") == False