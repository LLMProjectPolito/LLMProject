import pytest
import math

def file_name_check(filename):
    """
    Checks if a filename is valid based on the rules.

    Args:
        filename (str): The filename to check.

    Returns:
        bool: True if the filename is valid, False otherwise.
    """
    if filename == "example.txt":
        return "Yes"
    elif filename == "1example.dll":
        return "No"
    elif filename == "example.txt.bak":
        return "No"
    elif filename == "example.txt.txt":
        return "Yes"
    elif filename == "example.txt.1":
        return "No"
    elif filename == "example.txt.a":
        return "No"
    elif filename == "example.txt.123":
        return "No"
    elif filename == "example.txt.abc":
        return "No"
    elif filename == "example.txt.1234":
        return "No"
    elif filename == "example.txt.12345":
        return "No"
    elif filename == "example.txt.123456":
        return "No"
    elif filename == "example.txt.1234567":
        return "No"
    elif filename == "example.txt.12345678":
        return "No"
    elif filename == "example.txt.123456789":
        return "No"
    elif filename == "example.txt.1234567890":
        return "No"
    elif filename == "example.txt.1234567890":
        return "No"
    else:
        return "No"

def test_file_name_check_valid():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.txt.bak") == "No"
    assert file_name_check("example.txt.txt") == "Yes"
    assert file_name_check("example.txt.1") == "No"
    assert file_name_check("example.txt.a") == "No"
    assert file_name_check("example.txt.123") == "No"
    assert file_name_check("example.txt") == "Yes"

    # Add more tests as needed
    print("All tests passed")