import pytest
import math

def file_name_check(filename):
    """
    Checks if a filename is valid.
    """
    if filename.endswith((".txt", ".dll", ".exe")):
        return "Yes"
    else:
        return "No"

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("test.dll") == "Yes"
    assert file_name_check("a.exe") == "Yes"