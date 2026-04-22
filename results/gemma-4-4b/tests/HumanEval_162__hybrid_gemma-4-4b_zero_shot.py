
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5  # Replace your_module


class TestStringToMd5:

    def test_empty_string(self):
        assert string_to_md5("") is None

    def test_basic_string(self):
        assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

    def test_string_with_numbers(self):
        assert string_to_md5("1234567890") == 'e4d910a8b3789484e5695a3699d7d4f2'

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == '9927941607101d4b30d192f4785605e8'

    def test_string_with_mixed_characters(self):
        assert string_to_md5("This is a test!@#") == 'c9b23f4971c75e2a78c902469696a67e'

    def test_long_string(self):
        long_string = "This is a very long string to test the md5 function. " * 10
        md5_hash = hashlib.md5(long_string.encode()).hexdigest()
        assert string_to_md5(long_string) == md5_hash

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == '344935e361583b917748119e69c48778'

    def test_string_with_spaces_at_beginning_and_end(self):
        assert string_to_md5("   Hello world   ") == 'a9d81c087361712a4373290936513d97'

    def test_string_with_repeated_characters(self):
        assert string_to_md5("aaaaaaaaaa") == '6a625520f76d24262c59a76081c3f3e7'

    def test_string_with_newline_characters(self):
        assert string_to_md5("Line 1\nLine 2") == 'e69964a0a987163d3a19f709e1d5a69e'
    
    def test_different_case(self):
        assert string_to_md5("HeLlO wOrLd") == '78f65b9676068e942b748907a057b15b'

    def test_string_with_emoji(self):
        assert string_to_md5("Hello 😊 world") == '85b811592c4881f252375a8300c7c27e'

    def test_simple_string(self):
        assert string_to_md5("hello") == hashlib.md5("hello".encode()).hexdigest()

    def test_string_with_spaces(self):
        assert string_to_md5("Hello world") == hashlib.md5("Hello world".encode()).hexdigest()

    def test_string_with_special_characters(self):
        assert string_to_md5("!@#$%^&*()") == hashlib.md5("!@#$%^&*()".encode()).hexdigest()

    def test_string_with_unicode_characters(self):
        assert string_to_md5("你好世界") == hashlib.md5("你好世界".encode()).hexdigest()

    def test_long_string(self):
        long_string = "This is a very long string to test the function with." * 10
        expected_md5 = hashlib.md5(long_string.encode()).hexdigest()
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_mixed_characters(self):
        mixed_string = "123abc!@#$你好世界"
        expected_md5 = hashlib.md5(mixed_string.encode()).hexdigest()
        assert string_to_md5(mixed_string) == expected_md5

    def test_string_with_numbers_only(self):
        assert string_to_md5("1234567890") == hashlib.md5("1234567890".encode()).hexdigest()

    def test_string_with_alphabetic_only(self):
        assert string_to_md5("abcdefghijklmnopqrstuvwxyz") == hashlib.md5("abcdefghijklmnopqrstuvwxyz".encode()).hexdigest()
    
    def test_string_with_uppercase(self):
        assert string_to_md5("UPPERCASE") == hashlib.md5("UPPERCASE".encode()).hexdigest()

    def test_string_with_lowercase(self):
        assert string_to_md5("lowercase") == hashlib.md5("lowercase".encode()).hexdigest()
    
    def test_string_with_mixed_case(self):
      assert string_to_md5("MiXeD CaSe") == hashlib.md5("MiXeD CaSe".encode()).hexdigest()

    def test_string_with_newline_characters(self):
      assert string_to_md5("Line 1\nLine 2") == hashlib.md5("Line 1\nLine 2".encode()).hexdigest()

    def test_string_with_tab_characters(self):
      assert string_to_md5("Tabbed\tText") == hashlib.md5("Tabbed\tText".encode()).hexdigest()