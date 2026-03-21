import pytest

def test_words_string_with_commas():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

def test_words_string_with_spaces():
    assert words_string("One two three four five six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_with_both_commas_and_spaces():
    assert words_string("One, two three, four five, six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_with_leading_trailing_spaces():
    assert words_string("   One, two three, four five, six   ") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_with_empty_string():
    assert words_string("") == []

def test_words_string_with_single_word():
    assert words_string("Hello") == ["Hello"]

def test_words_string_with_single_word_and_trailing_comma():
    assert words_string("Hello,") == ["Hello"]

def test_words_string_with_single_word_and_trailing_space():
    assert words_string("Hello ") == ["Hello"]

def test_words_string_with_multiple_consecutive_commas():
    assert words_string("One,, two,, three,, four,, five,, six") == ["One", "", "two", "", "three", "", "four", "", "five", "", "six"]

def test_words_string_with_multiple_consecutive_spaces():
    assert words_string("One  two  three  four  five  six") == ["One", "two", "three", "four", "five", "six"]

def test_words_string_with_punctuation():
    assert words_string("One, two! three? four. five, six") == ["One", "two!", "three?", "four.", "five", "six"]

def test_words_string_with_consecutive_commas_at_start():
    assert words_string(",One, two, three") == ["", "One", "two", "three"]

def test_words_string_with_consecutive_commas_at_end():
    assert words_string("One, two, three,") == ["One", "two", "three", ""]

def test_words_string_with_consecutive_spaces_at_start():
    assert words_string(" One two three") == ["One", "two", "three"]

def test_words_string_with_consecutive_spaces_at_end():
    assert words_string("One two three ") == ["One", "two", "three"]

def test_words_string_with_consecutive_commas_and_spaces():
    assert words_string("One, , two , three") == ["One", "", "two", "", "three"]

def test_words_string_with_single_comma():
    assert words_string(",") == ["", ""]

def test_words_string_with_single_space():
    assert words_string(" ") == [""]

def test_words_string_with_multiple_consecutive_commas_and_spaces():
    assert words_string("One,,  two,,  three,,  four,,  five,,  six") == ["One", "", "two", "", "three", "", "four", "", "five", "", "six"]

def test_words_string_with_comma_at_start_and_end():
    assert words_string(",One, two, three,") == ["", "One", "two", "three", ""]

def test_words_string_with_space_at_start_and_end():
    assert words_string(" One two three ") == ["One", "two", "three"]

def test_words_string_with_non_string_input():
    with pytest.raises(TypeError):
        words_string(123)

def test_words_string_with_large_string():
    large_string = " ".join(["word"] * 1000)
    assert words_string(large_string) == ["word"] * 1000

def test_words_string_with_non_ascii_characters():
    assert words_string("Hëllo, Wørld") == ["Hëllo", "Wørld"]

def test_words_string_with_unicode_characters():
    assert words_string("Hëllo, Wørld") == ["Hëllo", "Wørld"]

def test_words_string_with_special_characters():
    assert words_string("Hëllo, Wørld\t\n") == ["Hëllo", "Wørld"]

def test_words_string_with_html_tags():
    assert words_string("<p>Hëllo, Wørld</p>") == ["<p>Hëllo", "Wørld</p>"]

def test_words_string_with_xml_tags():
    assert words_string("<tag>Hëllo, Wørld</tag>") == ["<tag>Hëllo", "Wørld</tag>"]

def test_words_string_with_json_data():
    assert words_string('{"key": "value"}') == ['{"key":', '"value"}']

def test_words_string_with_csv_data():
    assert words_string("Hëllo,Wørld") == ["Hëllo", "Wørld"]

def test_words_string_with_null_characters():
    assert words_string("Hëllo\0Wørld") == ["Hëllo", "Wørld"]

def test_words_string_with_non_printable_characters():
    assert words_string("Hëllo\x01Wørld") == ["Hëllo", "Wørld"]