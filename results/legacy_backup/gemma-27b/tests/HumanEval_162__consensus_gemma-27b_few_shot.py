import hashlib

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    expected_hash = 'd41d8cd98f00b204e9800998ecf8427e'
    assert string_to_md5(long_string) == expected_hash

def test_string_to_md5_with_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_string_to_md5_with_special_characters():
    assert string_to_md5('!@#$%^&*()') == '9f86d081884c7d659a2feaa0c55ad015'
    assert string_to_md5('!@#$%^') == 'c6a59499999999999999999999999999'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'