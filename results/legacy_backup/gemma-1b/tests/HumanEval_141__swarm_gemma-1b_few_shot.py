import pytest
import math

def file_name_check(filename):
    """
    Checks if a filename is valid.

    Args:
        filename (str): The filename to check.

    Returns:
        str: 'Yes' if the filename is valid, 'No' otherwise.
    """
    try:
        math.loads(filename)
        return 'Yes'
    except:
        return 'No'

def test_file_name_check():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt.txt") == 'Yes'
    assert file_name_check("example.txt.txt.txt") == 'No'

def test_file_name_check():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt.txt") == 'Yes'
    assert file_name_check("example.txt.txt.txt") == 'Yes'

def test_file_name_check():
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt.txt") == 'Yes'
    assert file_name_check("example.txt.txt.txt") == 'Yes'