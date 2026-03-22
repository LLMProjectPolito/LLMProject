import pytest

def test_solve_digits():
    """Test a string of only digits."""
    assert solve("1234") == "4321"

def test_solve_letters():
    """Test a string of only letters."""
    assert solve("ab") == "AB"

def test_solve_mixed():
    """Test a string with a mix of digits and letters."""
    assert solve("#a@C") == "#A@c"

def test_solve_no_letters():
    """Test a string with no letters (only digits or special characters)."""
    assert solve("!!!") == "!!!"

def test_solve_special_chars():
    """Test a string that contains no alphanumeric characters (only special characters)."""
    assert solve("---") == "---"

def test_solve_empty_string():
    """Test a string of length 0 (empty string)."""
    assert solve("") == ""

def test_solve_single_char():
    """Test a string with 1 character."""
    assert solve("A") == "A"

def test_solve_long_string():
    """Test a string with 100 characters."""
    assert solve("A" * 100) == "A" * 100

def test_solve_short_string():
    """Test a string with 3 characters."""
    assert solve("abc") == "ABC"

def test_solve_non_string():
    """Test a non-string input."""
    with pytest.raises(TypeError):
        solve(123)

def test_solve_none():
    """Test a None input."""
    with pytest.raises(TypeError):
        solve(None)

def test_solve_no_letters_digits():
    """Test a string with only digits."""
    assert solve("1234") == "4321"

def test_solve_no_letters_special_chars():
    """Test a string with only special characters."""
    assert solve("#$@") == "#$@"

def test_solve_no_letters_whitespace():
    """Test a string with only whitespace."""
    assert solve("   ") == "   "

def test_solve_all_uppercase_letters():
    """Test a string with all uppercase letters."""
    assert solve("ABC") == "abc"

def test_solve_all_lowercase_letters():
    """Test a string with all lowercase letters."""
    assert solve("abc") == "ABC"

def test_solve_mixed_case_letters():
    """Test a string with mixed case letters."""
    assert solve("AbC") == "aBC"

def test_solve_single_letter():
    """Test a string with a single letter."""
    assert solve("A") == "a"

def test_solve_multiple_letters():
    """Test a string with multiple letters."""
    assert solve("ABCD") == "aBCd"

def test_solve_multiple_consecutive_uppercase_letters():
    """Test a string with multiple consecutive uppercase letters."""
    assert solve("AAAA") == "aaaa"

def test_solve_multiple_consecutive_lowercase_letters():
    """Test a string with multiple consecutive lowercase letters."""
    assert solve("aaaa") == "AAAA"

def test_solve_multiple_consecutive_letters_different_cases():
    """Test a string with multiple consecutive letters of different cases."""
    assert solve("AbCd") == "aBCd"

def test_solve_empty_string_again():
    """Test a string of length 0 (empty string) again."""
    assert solve("") == ""