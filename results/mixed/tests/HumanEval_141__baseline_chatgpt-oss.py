# test_file_name_check.py
import pytest

# The function under test is assumed to be defined in a module named `file_name_check.py`
# located in the same directory as this test file.
from file_name_check import file_name_check


@pytest.mark.parametrize(
    "file_name,expected",
    [
        # ---- Valid file names -------------------------------------------------
        ("example.txt", "Yes"),          # basic valid case
        ("a.txt", "Yes"),                # minimal name before dot
        ("Abc.exe", "Yes"),              # uppercase start letter
        ("a1b2c3.dll", "Yes"),           # exactly three digits
        ("Z9Y8X7.txt", "Yes"),           # three digits scattered
        ("myFile123.txt", "Yes"),        # three digits at the end of the name part
        ("myFile.txt", "Yes"),           # no digits
        ("a1b2c.dll", "Yes"),            # two digits, valid extension
        # ---- Invalid because of digit count ----------------------------------
        ("ab1234.txt", "No"),            # four digits
        ("1234.txt", "No"),              # name starts with digit and >3 digits
        ("a1b2c3d4.exe", "No"),          # four digits total
        # ---- Invalid because of dot handling ---------------------------------
        ("exampletxt", "No"),            # missing dot
        ("example..txt", "No"),          # two consecutive dots
        ("example.tar.gz", "No"),        # more than one dot
        (".txt", "No"),                  # empty name before dot
        ("example.", "No"),              # empty extension after dot
        ("example..", "No"),             # empty extension and extra dot
        # ---- Invalid because of starting character ---------------------------
        ("1example.txt", "No"),          # starts with a digit
        ("_example.txt", "No"),          # starts with an underscore
        ("-example.txt", "No"),          # starts with a hyphen
        ("9.txt", "No"),                 # single digit name
        # ---- Invalid because of extension ------------------------------------
        ("example.pdf", "No"),           # unsupported extension
        ("example.tx", "No"),            # typo in extension
        ("example.txtt", "No"),          # extra character
        ("example.TXT", "No"),           # case‑sensitive extension
        ("example.Exe", "No"),           # mixed‑case extension
        ("example.dl", "No"),            # incomplete extension
        # ---- Combination edge cases -----------------------------------------
        ("a1b2c3d.txt", "No"),           # four digits even though extension ok
        ("a..txt", "No"),                # empty segment before second dot
        ("a.b.c.txt", "No"),             # more than one dot
        ("a1b2c3.", "No"),               # dot present but no extension
        ("a1b2c3.dl", "No"),             # wrong extension with valid digit count
    ],
)
def test_file_name_check(file_name, expected):
    """
    Verify that `file_name_check` returns the correct verdict ('Yes' or 'No')
    for a wide variety of inputs covering all validation rules.
    """
    assert file_name_check(file_name) == expected