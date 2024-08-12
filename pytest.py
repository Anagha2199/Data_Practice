import pytest

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("Please provide a string arg")
    return x.capitalize()
def isEven(num):
    if not isinstance(num,int):
        raise TypeError("Please provide a number")
    return num%2
def test_capital_case():
    assert capital_case("Python training")=="Python training"
