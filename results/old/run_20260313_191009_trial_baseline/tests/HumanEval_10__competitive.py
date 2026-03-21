import pytest

def test_is_palindrome_empty_string():
    assert is_palindrome('') == True

def test_is_palindrome_single_character():
    assert is_palindrome('a') == True

def test_is_palindrome_palindrome():
    assert is_palindrome('madam') == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome('hello') == False

def test_is_palindrome_numbers():
    assert is_palindrome('12321') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Madam') == False

def test_is_palindrome_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == False

def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_character():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_palindrome():
    assert make_palindrome('madam') == 'madam'

def test_make_palindrome_not_palindrome():
    assert make_palindrome('cat') == 'catac'

def test_make_palindrome_long_string():
    assert make_palindrome('abcdefgh') == 'abcdefghhgfedcba'

def test_make_palindrome_mixed_case():
    assert make_palindrome('Madam') == 'MadamaDam'

def test_make_palindrome_punctuation():
    assert make_palindrome('A man, a plan, a canal: Panama') == 'A man, a plan, a canal: Panamapacanal a ,nalp a ,nam A'