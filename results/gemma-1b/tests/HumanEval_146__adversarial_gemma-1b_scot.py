
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

```python
import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        num_str = str(abs(num))
        if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_single_element_greater_than_10_odd():
    assert specialFilter([15]) == 1

def test_specialFilter_single_element_odd_first_digit():
    assert specialFilter([15]) == 0

def test_specialFilter_single_element_odd_last_digit():
    assert specialFilter([15]) == 0

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 9]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 11]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 13]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 15]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 17]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 19]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 21]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 23]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 25]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 27]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 29]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 31]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 33]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 35]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 37]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 39]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 41]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 43]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 45]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 47]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 49]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 51]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 53]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 55]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 57]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 59]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 61]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 63]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 65]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 67]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 69]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 71]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 73]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 75]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 77]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 79]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 89]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 91]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 93]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 95]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 97]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 99]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 101]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 103]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 105]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 107]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 109]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 111]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 113]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 115]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 117]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 119]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 121]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 123]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 125]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 127]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 129]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 131]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 133]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 135]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 137]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 139]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 141]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 143]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 145]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 147]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 149]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 151]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 153]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 155]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 157]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 159]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 161]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 163]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 165]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 167]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 169]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 171]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 173]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 175]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 177]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 179]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 181]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 183]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 185]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 187]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 189]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 191]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 193]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 195]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 197]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 199]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 201]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 203]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 205]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 207]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 209]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 211]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 213]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 215]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 217]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 219]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 221]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 223]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 225]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 227]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 229]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 231]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 233]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 235]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 237]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 239]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 241]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 243]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 245]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 247]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 249]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 251]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 253]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 255]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 257]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 259]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 261]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 263]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 265]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 267]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 269]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 271]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 273]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 275]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 277]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 279]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 281]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 283]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 285]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 287]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 289]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 291]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 293]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 295]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 297]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 299]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 301]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 303]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 305]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 307]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 309]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 311]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 313]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 315]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 317]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 319]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 321]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 323]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 325]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 327]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 329]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 331]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 333]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 335]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 337]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 339]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 341]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 343]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 345]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 347]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 349]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 351]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 353]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 355]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 357]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 359]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 361]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 363]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 365]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 367]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 369]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 371]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 373]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 375]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 377]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 379]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 381]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 383]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 385]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 387]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 389]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 391]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 393]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 395]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 397]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 399]) == 0
    assert specialFilter([1, 2, 3, 4, 5