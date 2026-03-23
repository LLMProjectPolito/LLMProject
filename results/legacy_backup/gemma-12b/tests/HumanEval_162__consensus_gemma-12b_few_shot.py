import hashlib

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'ba7816bf8f01cfea414140de5dae2223'
    assert string_to_md5('12345') == '5d414c7b1191c631451e83c36493f360'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '99d83136999999999999999999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    assert string_to_md5(long_string) == '99999999999999999999999999999999' # Placeholder - actual hash will vary

def test_string_to_md5_numbers_only():
    assert string_to_md5('1111111111') == '6f849399499999999999999999999999'