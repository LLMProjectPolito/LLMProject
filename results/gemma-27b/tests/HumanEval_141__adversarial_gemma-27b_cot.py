import pytest

def test_valid_file_names():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("MyFile.exe") == "Yes"
    assert file_name_check("document1.dll") == "Yes"
    assert file_name_check("A.txt") == "Yes"
    assert file_name_check("file123.txt") == "Yes"

def test_invalid_file_names_digit_count():
    assert file_name_check("1234example.txt") == "No"
    assert file_name_check("example1234.txt") == "No"
    assert file_name_check("123example1.txt") == "No"

def test_invalid_file_names_dot_count():
    assert file_name_check("example.txt.txt") == "No"
    assert file_name_check("exampletxt") == "No"
    assert file_name_check(".txt") == "No"

def test_invalid_file_names_empty_substring_before_dot():
    assert file_name_check(".txt") == "No"
    assert file_name_check("example.") == "No"

def test_invalid_file_names_starting_with_digit():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2file.exe") == "No"

def test_invalid_file_names_invalid_extension():
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("file.jpg") == "No"
    assert file_name_check("document.png") == "No"

def test_invalid_file_names_empty_file_name():
    assert file_name_check("") == "No"

def test_invalid_file_names_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("file@name.exe") == "No"

def test_valid_file_names_uppercase():
    assert file_name_check("Example.txt") == "Yes"
    assert file_name_check("MYFILE.exe") == "Yes"

def test_valid_file_names_mixed_case():
    assert file_name_check("ExAmPlE.txt") == "Yes"
    assert file_name_check("fIlE1.dll") == "Yes"