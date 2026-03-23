import hashlib

def test_string_to_md5_valid():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'ba7816bf8f01cfea414140de5dae2223'
    assert string_to_md5('12345') == '5d414c7b11979469fb0c228049a87c6a'
    assert string_to_md5('aA') == 'd14a028c2a3a2bc9476102bb28823406'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_special_chars():
    assert string_to_md5('!@#$%^') == '9d0b2b99432939999999999999999999'
    assert string_to_md5('你好世界') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_with_spaces():
    assert string_to_md5('  test  ') == 'd14a028c2a3a2bc9476102bb28823406'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_md5