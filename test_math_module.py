import pytest
from math_module import factorial, is_even

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False