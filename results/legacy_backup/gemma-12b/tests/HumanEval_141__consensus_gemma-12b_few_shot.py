import re

def test_valid_filename():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("my_file.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("longname.txt") == "Yes"
    assert file_name_check("valid1.txt") == "Yes"
    assert file_name_check("valid22.txt") == "Yes"
    assert file_name_check("valid333.txt") == "Yes"

def test_invalid_filename_too_many_digits():
    assert file_name_check("1234example.txt") == "No"

def test_invalid_filename_no_dot():
    assert file_name_check("example") == "No"

def test_invalid_filename_empty_before_dot():
    assert file_name_check(".txt") == "No"

def test_invalid_filename_dot_at_start():
    assert file_name_check(".txt") == "No"

def test_invalid_filename_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"

def test_invalid_filename_extension_case():
    assert file_name_check("example.TXT") == "No"
    assert file_name_check("example.EXE") == "No"
    assert file_name_check("example.DLL") == "No"

def test_invalid_filename_starts_with_digit():
    assert file_name_check("1example.txt") == "No"

def test_invalid_filename_empty_string():
    assert file_name_check("") == "No"

def test_invalid_filename_only_dot():
    assert file_name_check(".") == "No"