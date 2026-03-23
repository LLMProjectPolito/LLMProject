import pytest

def test_valid_file_names():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'
    assert file_name_check("file123.txt") == 'Yes'
    assert file_name_check("a123.txt") == "Yes"
    assert file_name_check("A1B2.dll") == "Yes"
    assert file_name_check("Example.txt") == "Yes"
    assert file_name_check("MYFILE.exe") == "Yes"
    assert file_name_check("ANOTHERFILE.dll") == "Yes"
    assert file_name_check("ExAmPlE.txt") == "Yes"
    assert file_name_check("MyFiLe.exe") == "Yes"
    assert file_name_check("AnOtHeRfIlE.dll") == "Yes"
    assert file_name_check("ExAm1PlE.txt") == "Yes"
    assert file_name_check("MyFi1e.exe") == "Yes"
    assert file_name_check("An0therFiLe.dll") == "Yes"
    assert file_name_check("A1B2c3.txt") == "Yes"
    assert file_name_check("a1B2c3.exe") == "Yes"
    assert file_name_check("A1b2C3.dll") == "Yes"

def test_invalid_file_names_digit_count():
    assert file_name_check("1234example.txt") == 'No'
    assert file_name_check("example1234.exe") == 'No'
    assert file_name_check("a1234.dll") == "No"
    assert file_name_check("examp1234le.exe") == "No"

def test_invalid_file_names_dot_count():
    assert file_name_check("example.txt.txt") == 'No'
    assert file_name_check("exampletxt") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("My.File.exe") == "No"
    assert file_name_check("Another.File.dll") == "No"

def test_invalid_file_names_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("2MyFile.exe") == 'No'
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("2MyFile.exe") == "No"
    assert file_name_check("3AnotherFile.dll") == "No"

def test_invalid_file_names_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_names_invalid_extension():
    assert file_name_check("example.pdf") == 'No'
    assert file_name_check("file.jpg") == 'No'
    assert file_name_check("example.pdf") == "No"
    assert file_name_check("MyFile.jpg") == "No"
    assert file_name_check("AnotherFile.png") == "No"

def test_edge_cases():
    assert file_name_check("a.txt") == 'Yes'
    assert file_name_check("A.exe") == 'Yes'
    assert file_name_check("abc.dll") == 'Yes'
    assert file_name_check("example1.txt") == 'Yes'
    assert file_name_check("example12.exe") == 'Yes'
    assert file_name_check("example123.dll") == 'Yes'
    assert file_name_check("example.TXT") == 'No'
    assert file_name_check("example.ExE") == 'No'
    assert file_name_check("example.DlL") == 'No'

def test_invalid_file_name_empty_string():
    assert file_name_check("") == "No"

def test_invalid_file_name_special_characters():
    assert file_name_check("example!.txt") == "No"
    assert file_name_check("MyFile@.exe") == "No"
    assert file_name_check("AnotherFile#.dll") == "No"