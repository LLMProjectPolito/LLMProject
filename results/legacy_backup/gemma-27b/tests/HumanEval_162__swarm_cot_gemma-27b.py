import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

@pytest.mark.parametrize("long_string_length", [10000, 100000])
def test_string_to_md5_very_long_string(long_string_length):
    """Test with a very long string to check for potential performance issues or buffer overflows."""
    long_string = "a" * long_string_length
    expected_md5 = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == expected_md5