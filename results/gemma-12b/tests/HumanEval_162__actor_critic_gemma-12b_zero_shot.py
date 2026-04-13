
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
import secrets

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

class TestStringtoMD5:
    def test_valid_string(self):
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_empty_string(self):
        assert string_to_md5('') is None

    def test_string_with_spaces(self):
        assert string_to_md5('  ') == 'd14a028c2a3a2bc9476102bb288234c4'

    def test_string_with_special_characters(self):
        assert string_to_md5('!@#$%^&*()') == 'a805c549999999999999999999999999'

    def test_string_with_unicode_characters(self):
        assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

    def test_string_with_numbers(self):
        assert string_to_md5('1234567890') == 'd1e2f3e4d5c6b7a8901234567890'

    def test_string_with_mixed_characters(self):
        assert string_to_md5('Hello123World!') == 'b10a8db164e0754105b7a99be72e3fe5'

    def test_long_string(self):
        long_string = secrets.token_hex(2048)
        md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == md5_hash

    def test_string_with_newline_characters(self):
        assert string_to_md5("Hello\nWorld") == '94f19999999999999999999999999999'

    def test_string_with_tab_characters(self):
        assert string_to_md5("Hello\tWorld") == '94f19999999999999999999999999999'

    def test_single_character_string(self):
        assert string_to_md5('a') == 'ba7816bf8f01cfea414140de5dae2223'

    def test_case_sensitivity(self):
        assert string_to_md5('Hello') != string_to_md5('hello')

    def test_string_with_only_whitespace(self):
        assert string_to_md5("   \t\n") == 'e5d78999999999999999999999999999'