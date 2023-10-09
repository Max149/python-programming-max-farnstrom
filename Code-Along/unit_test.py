from my_module import square

def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25
    assert square(-2) == 4
    assert square(-5) == 25
    assert square(0) == 0

def test_negative_square():
    assert square(2) == 4
    assert square(5) == 25

def test_zero_square():
    assert square(0) == 0


# import math


# print(my_module.sqrt(9))
# print(my_module.square(9))
# print(math.sqrt(9))