import pytest
import math

def is_valid_code(code):
    """
    Checks if the given code is valid.
    """
    try:
        exec(code)
        return True
    except Exception:
        return False

def is_valid_file(filename):
    """
    Checks if the given filename is valid.
    """
    if not filename:
        return "No"
    if not filename[0].isalpha():
        return "No"
    if "." not in filename:
        return "No"
    parts = filename.split(".")
    if len(parts) != 2:
        return "No"
    if not parts[0].isalpha():
        return "No"
    if parts[1].lower() not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"

@pytest.mark.parametrize(
    "rules, expected",
    [
        (
            "if len(file_name) > 3: return 'No'",
            "No",
        ),
        (
            "if "." not in file_name: return 'No'",
            "No",
        ),
        (
            "if not file_name[0]: return 'No'",
            "No",
        ),
        (
            "parts = file_name.split('.')",
            "No",
        ),
        (
            "if len(parts) != 2: return 'No'",
            "No",
        ),
        (
            "if not parts[0].isalpha(): return 'No'",
            "No",
        ),
        (
            "if parts[1].lower() not in ['txt', 'exe', 'dll']: return 'No'",
            "No",
        ),
        (
            "Yes",
        ),
        (
            "if "." not in file_name: return 'No'",
            "No",
        ),
        (
            "if not file_name[:3].isalpha(): return 'No'",
            "No",
        ),
        (
            "parts = file_name[3:].split('.')",
            "No",
        ),
        (
            "if not parts[0].isalpha(): return 'No'",
            "No",
        ),
        (
            "if not parts[0]: return 'No'",
            "No",
        ),
        (
            "if parts[-1] not in ['txt', 'exe', 'dll']: return 'No'",
            "No",
        ),
        "Yes",
    ],
)

def test_is_valid_code():
    assert is_valid_code("test.txt") == "Yes"
    assert is_valid_code("test.exe") == "Yes"
    assert is_valid_code("test.dll") == "Yes"
    assert is_valid_code("test.txt.exe") == "No"
    assert is_valid_code("test.txt") == "No"
    assert is_valid_code("test.txt.exe") == "No"
    assert is_valid_code("test.txt.dll") == "No"
    assert is_valid_code("test.txt") == "No"
    assert is_valid_code("test.txt.exe") == "No"
    assert is_valid_code("test.txt.dll") == "No"
    assert is_valid_code("test.txt") == "No"
    assert is_valid_code("test.txt.exe") == "No"
    assert is_valid_code("test.txt.dll") == "No"
    assert is_valid_code("test.txt") == "No"
    assert is_valid_code("test.txt.exe") == "No"
    assert is_valid_code("test.txt.dll") == "No"