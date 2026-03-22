import hashlib
import pytest

# Assume the implementation is available in a module named `solution`.
from solution import string_to_md5


@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("abc", "900150983cd24fb0d6963f7d28e17f72"),
        ("1234567890", "e807f1fcf82d132f9bb018ca6738a19f"),
        ("", None),  # empty string case
        (" ", "7215ee9c7d9dc229d2921a40e899ec5f"),
        ("\n", "68b329da9893e34099c7d8ad5cb9c940"),
        ("こんにちは", "9d735278cfbdb946834416adfb5aaf6c"),
        ("a" * 1000, hashlib.md5(("a" * 1000).encode("utf-8")).hexdigest()),
    ],
)
def test_string_to_md5_known_values(input_text, expected):
    """Validate known hash outputs and the empty‑string special case."""
    assert string_to_md5(input_text) == expected


def test_output_type_and_length():
    """The function should return a 32‑character hexadecimal string for non‑empty input."""
    result = string_to_md5("pytest")
    assert isinstance(result, str)
    assert len(result) == 32
    # ensure all characters are valid hex digits
    int(result, 16)  # will raise ValueError if non‑hex characters are present


@pytest.mark.parametrize("input_text", ["test", " another test ", "line1\nline2", "🚀🌟"])
def test_consistency_with_hashlib(input_text):
    """Result must match hashlib.md5 for the same UTF‑8 encoding."""
    expected = hashlib.md5(input_text.encode("utf-8")).hexdigest()
    assert string_to_md5(input_text) == expected


def test_non_string_input_raises():
    """Passing a non‑string (e.g., bytes, int) should raise a TypeError."""
    for bad_input in [b"bytes", 123, None, 3.14, ["list"], {"dict": "value"}]:
        with pytest.raises(TypeError):
            string_to_md5(bad_input)


def test_whitespace_handling():
    """Whitespace characters are part of the input and affect the hash."""
    text = "  leading and trailing spaces  "
    expected = hashlib.md5(text.encode("utf-8")).hexdigest()
    assert string_to_md5(text) == expected