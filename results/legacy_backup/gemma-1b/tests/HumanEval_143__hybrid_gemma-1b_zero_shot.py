import pytest

def words_in_sentence(sentence):
    words = sentence.split()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)

@pytest.mark.parametrize(
    "sentence, expected_output",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "hello"),
        ("a b c d e", "a"),
        ("123456789", "123456789"),
        ("abc", "abc"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
        ("19", "19"),
        ("20", "20"),
    ],
)
def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == "hello"
    assert words_in_sentence("a b c d e") == "a"
    assert words_in_sentence("123456789") == "123456789"
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("1") == "1"
    assert words_in_sentence("2") == "2"
    assert words_in_sentence("3") == "3"
    assert words_in_sentence("4") == "4"
    assert words_in_sentence("5") == "5"
    assert words_in_sentence("6") == "6"
    assert words_in_sentence("7") == "7"
    assert words_in_sentence("8") == "8"
    assert words_in_sentence("9") == "9"