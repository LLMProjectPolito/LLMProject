import pytest
from hashlib import md5

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    encoded_text = text.encode('utf-8')
    # print(f"Encoded text: {encoded_text}")  # Debugging line
    return md5(encoded_text).hexdigest()

# Basic Strings
def test_basic_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_spaces():
    assert string_to_md5("  Hello world  ") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "d9b13a83b8b1f4919991a9a94148994f"

def test_string_with_numbers():
    assert string_to_md5("1234567890") == "5d41402abc4b2a76b9719d911017c592"

def test_string_with_mixed_case():
    assert string_to_md5("Hello World") == "6cd3556deb0da54bca060b4c39479839"

# Edge Cases
def test_empty_string():
    assert string_to_md5("") is None

# Unicode Strings
def test_unicode_string():
    assert string_to_md5("你好世界") == "5994471abb01112afcc18159f6cc74b4"

def test_complex_unicode():
    assert string_to_md5("नमस्ते🙏") == "9f86d081884c7d659a2feaa0c55ad015"

# Long Strings
def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"

def test_very_long_string():
    very_long_string = "a" * 1024 * 1024  # 1MB
    assert string_to_md5(very_long_string) == "99b99999999999999999999999999999"

# Other
def test_string_with_newline():
    assert string_to_md5("Hello\nWorld") == "6a2da209439339896994b99999999999"

def test_whitespace_string():
    assert string_to_md5("   ") == "6f9d8f329f9a8b9a9b9a8b9a8b9a8b9a"