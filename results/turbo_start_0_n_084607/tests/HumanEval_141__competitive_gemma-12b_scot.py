import pytest

def test_valid_file_name():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("document.dll") == "Yes"
    assert file_name_check("image.exe") == "Yes"
    assert file_name_check("a.txt") == "Yes"
    assert file_name_check("A.TXT") == "Yes"
    assert file_name_check("long_file_name.txt") == "Yes"
    assert file_name_check("valid12.txt") == "Yes"

def test_invalid_file_name_too_many_digits():
    assert file_name_check("1234.txt") == "No"
    assert file_name_check("12345.txt") == "No"

def test_invalid_file_name_no_dot():
    assert file_name_check("example") == "No"
    assert file_name_check("exampletxt") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.dll") == "No"
    assert file_name_check("example..txt") == "No"

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check(".exe") == "No"
    assert file_name_check(".dll") == "No"

def test_invalid_file_name_not_letter_before_dot():
    assert file_name_check("1.txt") == "No"
    assert file_name_check("_.txt") == "No"
    assert file_name_check("!txt") == "No"

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("example.jpg") == "No"
    assert file_name_check("example.dat") == "No"
    assert file_name_check("example.") == "No"

def test_invalid_file_name_extension_case():
    assert file_name_check("example.TXT") == "No"
    assert file_name_check("example.EXE") == "No"
    assert file_name_check("example.DLL") == "No"

def test_empty_file_name():
    assert file_name_check("") == "No"