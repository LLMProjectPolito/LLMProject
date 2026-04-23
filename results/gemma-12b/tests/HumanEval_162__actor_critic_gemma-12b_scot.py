
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

class TestStringtoMD5:
    def test_valid_string(self):
        assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_empty_string(self):
        assert string_to_md5('') is None

    def test_special_characters(self):
        assert string_to_md5('!@#') == '6e34ebcbdf0a8f0e19634a3a4a29a393'

    def test_numbers_string(self):
        assert string_to_md5('1234567890') == 'd162b37f99a33269990436196239993a'

    def test_alphanumeric_string(self):
        assert string_to_md5('a1!@#') == '9949949949949949949949949949949'

    def test_long_string(self):
        long_string = "This is a very long string to test the function with a large input." * 100
        expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_md5

    def test_unicode_string(self):
        assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

    def test_case_sensitivity(self):
        assert string_to_md5('Hello') != string_to_md5('hello')

    def test_whitespace_handling(self):
        assert string_to_md5('  Hello world  ') == hashlib.md5(('Hello world').encode('utf-8')).hexdigest()

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            string_to_md5(123)