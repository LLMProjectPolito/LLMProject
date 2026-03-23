def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("MyFile.exe") == 'Yes'
    assert file_name_check("document1.dll") == 'Yes'
    assert file_name_check("A.txt") == 'Yes'
    assert file_name_check("file123.txt") == 'Yes'

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.backup") == 'No'

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("123file.txt") == 'No'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("example1234.txt") == 'No'

def test_invalid_file_name_invalid_extension():
    assert file_name_check("example.jpg") == 'No'
    assert file_name_check("example.pdf") == 'No'

def test_invalid_file_name_empty_string():
    assert file_name_check("") == 'No'

def test_invalid_file_name_extension_case_sensitive():
    assert file_name_check("example.Txt") == 'No'
    assert file_name_check("example.EXE") == 'No'
    assert file_name_check("example.DLL") == 'No'