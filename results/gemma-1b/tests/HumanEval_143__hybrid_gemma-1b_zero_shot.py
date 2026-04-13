
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

```python
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
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "hello"),
        ("a b c d e", "a"),
        ("12345", "12345"),
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
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),
        ("30", "30"),
        ("31", "31"),
        ("32", "32"),
        ("33", "33"),
        ("34", "34"),
        ("35", "35"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
        ("45", "45"),
        ("46", "46"),
        ("47", "47"),
        ("48", "48"),
        ("49", "49"),
        ("50", "50"),
        ("51", "51"),
        ("52", "52"),
        ("53", "53"),
        ("54", "54"),
        ("55", "55"),
        ("56", "56"),
        ("57", "57"),
        ("58", "58"),
        ("59", "59"),
        ("60", "60")
    ]

Suite 2:
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
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "hello"),
        ("a b c d e", "a"),
        ("12345", "12345"),
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
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),
        ("30", "30"),
        ("31", "31"),
        ("32", "32"),
        ("33", "33"),
        ("34", "34"),
        ("35", "35"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
        ("45", "45"),
        ("46", "46"),
        ("47", "47"),
        ("48", "48"),
        ("49", "49"),
        ("50", "50"),
        ("51", "51"),
        ("52", "52"),
        ("53", "53"),
        ("54", "54"),
        ("55", "55"),
        ("56", "56"),
        ("57", "57"),
        ("58", "58"),
        ("59", "59"),
        ("60", "60")
    ]

@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("hello world", "hello"),
        ("a b c d e", "a"),
        ("12345", "12345"),
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
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),
        ("30", "30"),
        ("31", "31"),
        ("32", "32"),
        ("33", "33"),
        ("34", "34"),
        ("35", "35"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39