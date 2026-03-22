import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("image.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_name.exe") == "Yes"
    assert file_name_check("file123.txt") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("1234.txt") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_file_name_not_letter_before_dot():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("_example.txt") == "No"
    assert file_name_check(" example.txt") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.") == "No"

def test_invalid_file_name_empty_extension():
    assert file_name_check("example.") == "No"

def test_file_name_with_digits_and_letters():
    assert file_name_check("file1.txt") == "Yes"
    assert file_name_check("file23.exe") == "Yes"
    assert file_name_check("file12.dll") == "Yes"
    assert file_name_check("1file.txt") == "No"
    assert file_name_check("file1234.txt") == "No"