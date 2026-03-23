import hashlib
import pytest

# ----------------------------------------------------------------------
# Import the function under test.
# The implementation should be located in a module that is importable from
# the test directory.  Adjust the import statement to match the actual
# file name (e.g., `from my_module import string_to_md5`).
# ----------------------------------------------------------------------
from string_to_md5 import string_to_md5   # <-- replace with the correct module name


def _md5_hexdigest(text: str) -> str:
    """
    Helper that returns the canonical MD5 hex digest for *text* using
    Python's ``hashlib`` – this is the source of truth for the expected
    values in the parametrised tests.
    """
    return hashlib.md5(text.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------
# 1️⃣  Basic correctness – known inputs and their expected digests
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("", None),                                   # empty string special case
        ("a", "0cc175b9c0f1b6a831c399e269772661"),
        ("abc", "900150983cd24fb0d6963f7d28e17f72"),
        ("1234567890", "e807f1fcf82d132f9bb018ca6738a19f"),
        ("   leading and trailing   ", "c5e5c5c5c8c0b6c2c5e6c5c5c5c5c5c5"),  # placeholder, will be overridden
        ("こんにちは", "9d735278cfbdb946834416adfb5aaf6c"),
        ("😀🚀🌟", "c2d5c5c5c5c5c5c5c5c5c5c5c5c5c5c5"),  # placeholder, will be overridden
    ],
)
def test_known_hashes(input_text: str, expected: str):
    """
    Verify that ``string_to_md5`` returns the correct MD5 hex digest for a
    collection of representative strings, and that it returns ``None`` for
    an empty string.
    """
    # For the two placeholder entries we compute the expected value on‑the‑fly
    if expected is None or expected.startswith("c5e5") or expected.startswith("c2d5"):
        expected = _md5_hexdigest(input_text) if input_text else None

    assert string_to_md5(input_text) == expected


# ----------------------------------------------------------------------
# 2️⃣  Return type & format
# ----------------------------------------------------------------------
def test_return_type_and_format():
    """
    The function should return a 32‑character lower‑case hexadecimal string
    for any non‑empty input.
    """
    result = string_to_md5("pytest")
    assert isinstance(result, str), "Result should be a string"
    assert len(result) == 32, "MD5 hex digest must be 32 characters long"
    # all characters must be valid hex digits
    assert all(c in "0123456789abcdef" for c in result)


# ----------------------------------------------------------------------
# 3️⃣  Unicode handling
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "unicode_text",
    [
        "ñáéíóúüÑÁÉÍÓÚÜ",
        "Привет мир",
        "مرحبا بالعالم",
        "𐍈𐍉𐍊",          # characters outside the BMP
        "😀🚀🌟",          # emojis
    ],
)
def test_unicode_strings(unicode_text: str):
    """
    Ensure that Unicode strings are correctly encoded (UTF‑8) before hashing.
    """
    expected = _md5_hexdigest(unicode_text)
    assert string_to_md5(unicode_text) == expected


# ----------------------------------------------------------------------
# 4️⃣  Large input handling
# ----------------------------------------------------------------------
def test_long_string():
    """
    Hash a very long string (several megabytes) to confirm that the
    implementation works for large inputs without raising errors.
    """
    long_text = "a" * 5_000_000  # 5 MiB of the character 'a'
    expected = _md5_hexdigest(long_text)
    assert string_to_md5(long_text) == expected


# ----------------------------------------------------------------------
# 5️⃣  Non‑string input – defensive programming
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "bad_input",
    [
        123,                     # int
        45.6,                    # float
        b"bytes",                # bytes
        None,                    # NoneType
        ["list", "of", "str"],   # list
        {"key": "value"},        # dict
    ],
)
def test_non_string_input_raises(bad_input):
    """
    The contract of the function is to accept only strings.  Supplying any
    other type should raise a ``TypeError`` (or a subclass thereof).  If the
    implementation silently converts the value, the test will fail – this
    encourages explicit input validation.
    """
    with pytest.raises(TypeError):
        string_to_md5(bad_input)


# ----------------------------------------------------------------------
# 6️⃣  Idempotence – calling the function repeatedly yields the same result
# ----------------------------------------------------------------------
def test_idempotence():
    """
    Re‑invoking the function with the same argument must always produce the
    same output.
    """
    text = "repeatable test string"
    first = string_to_md5(text)
    for _ in range(10):
        assert string_to_md5(text) == first