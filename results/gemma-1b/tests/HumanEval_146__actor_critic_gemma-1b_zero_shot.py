
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

def test_empty_array():
    assert specialFilter([]) == 0

def test_single_element():
    assert specialFilter([15]) == 1

def test_positive_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([1, 2, 3, 4, 5]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 14]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 15]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 16]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 17]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 21]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 23]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 25]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 27]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 29]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 31]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 33]) == 1
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 35]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 37]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 39]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 41]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 43]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 45]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 47]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 49]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 51]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 53]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 55]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 57]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 59]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 61]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 63]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 65]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 67]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 69]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 71]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 73]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 75]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 77]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 79]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 81]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 83]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 85]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 87]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 89]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 91]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 93]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 95]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 97]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 99]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 101]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 103]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 105]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 107]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 109]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 111]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 113]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 115]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 117]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 119]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 121]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 123]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 125]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 127]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 129]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 131]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 133]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 135]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 137]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 139]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 141]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 143]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 145]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 147]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 149]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 151]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 153]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 155]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 157]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 159]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 161]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 163]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 165]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 167]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 169]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 171]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 173]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 175]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 177]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 179]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 181]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 183]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 185]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 187]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 189]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 191]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 193]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 195]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 197]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 199]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 201]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 203]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 205]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 207]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 209]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 211]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 213]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 215]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 217]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 219]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 221]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 223]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 225]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 227]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 229]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 231]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 233]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 235]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 237]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 239]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 241]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 243]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 245]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 247]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 249]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 251]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 253]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 255]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 257]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 259]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 261]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 263]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 265]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 267]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 269]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 271]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 273]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 275]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 277]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 279]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 281]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 283]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 285]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 287]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 289]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 291]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 293]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 295]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 297]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 299]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 301]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 303]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 305]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 307]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 309]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 311]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 313]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 315]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 317]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 319]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 321]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 323]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 325]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 327]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 329]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 331]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 333]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 335]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 337]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 339]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 341]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 343]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 345]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 347]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 349]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 351]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 353]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 355]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 357]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 359]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 361]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 363]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 365]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 367]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 369]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 371]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 373]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 375]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 377]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 379]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 381]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 383]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 385]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 387]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 389]) == 0
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 391]) == 0
    assert specialFilter([1, 2, 3, 4,