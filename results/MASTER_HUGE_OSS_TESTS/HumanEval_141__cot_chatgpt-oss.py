import pytest

# Assume file_name_check is imported from the module where it is defined
# from your_module import file_name_check


@pytest.mark.parametrize(
    "file_name,expected",
    [
        # Valid cases
        ("example.txt", "Yes"),
        ("Example.exe", "Yes"),
        ("a1b2c3.dll", "Yes"),          # exactly three digits
        ("A.txt", "Yes"),               # single letter name
        ("Z9Y8X7.exe", "Yes"),          # three digits, mixed case
        ("myFile123.txt", "Yes"),       # three digits at end
        # Invalid: more than three digits
        ("a1b2c3d4.txt", "No"),
        ("1234.txt", "No"),
        ("file1234.exe", "No"),
        # Invalid: missing dot
        ("exampletxt", "No"),
        ("example", "No"),
        # Invalid: multiple dots
        ("example.tar.gz", "No"),
        ("my.file.txt", "No"),
        # Invalid: empty name before dot
        (".txt", "No"),
        (".exe", "No"),
        # Invalid: empty extension after dot
        ("example.", "No"),
        ("test.", "No"),
        # Invalid: name does not start with a letter
        ("1example.txt", "No"),
        ("_example.dll", "No"),
        ("-example.exe", "No"),
        # Invalid: unsupported extension
        ("example.pdf", "No"),
        ("example.doc", "No"),
        ("example.jpeg", "No"),
        # Invalid: case-sensitive extension
        ("example.TXT", "No"),
        ("example.Exe", "No"),
        ("example.DLL", "No"),
        # Edge: dot at the end of name but with valid extension length (should be invalid)
        ("example.t", "No"),
        ("example.tx", "No"),
        # Edge: name with allowed characters but extra dot in extension part
        ("example.t.xt", "No"),
    ],
)
def test_file_name_check(file_name, expected):
    assert file_name_check(file_name) == expected


def test_boundary_digit_counts():
    # Exactly three digits anywhere in the string should be allowed
    assert file_name_check("a1b2c3.txt") == "Yes"
    # Four digits should be rejected
    assert file_name_check("a1b2c3d4.txt") == "No"
    # Digits spread across name and extension (extension digits not allowed by spec)
    # Since extension must be one of the listed strings, any digit there makes it invalid
    assert file_name_check("file1.tx1") == "No"


def test_start_letter_cases():
    # Uppercase start is valid
    assert file_name_check("Zfile.txt") == "Yes"
    # Lowercase start is valid
    assert file_name_check("zfile.txt") == "Yes"
    # Non‑letter start is invalid
    for prefix in ["9", "_", "-", " "]:
        assert file_name_check(f"{prefix}file.txt") == "No"


def test_extension_exact_match():
    # Only the exact lower‑case extensions are accepted
    for ext in ["txt", "exe", "dll"]:
        assert file_name_check(f"valid.{ext}") == "Yes"
    # Any deviation (uppercase, extra characters) should be rejected
    assert file_name_check("valid.TxT") == "No"
    assert file_name_check("valid.txtx") == "No"
    assert file_name_check("valid.") == "No"