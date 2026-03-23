import pytest
import hashlib

def test_string_to_md5_known_value():
    """Verify known MD5 hash for a simple string."""
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_empty_string():
    """Empty input should return None."""
    assert string_to_md5("") is None

@pytest.mark.parametrize(
    "length",
    [
        1000,   # medium‑size long string
        10000,  # very long string
    ],
)
def test_string_to_md5_long_strings(length):
    """Check MD5 calculation for long strings of varying lengths."""
    long_string = "a" * length
    expected_md5 = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == expected_md5