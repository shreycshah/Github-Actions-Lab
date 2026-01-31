import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 4) == 6
    assert calculator.fun1(5, 2) == 7
    assert calculator.fun1(-2, 2) == 0
    assert calculator.fun1(-1, -2) == -3

def test_fun2():
    assert calculator.fun2(2, 4) == -2
    assert calculator.fun2(6, 0) == 6
    assert calculator.fun2(-1, 2) == -3
    assert calculator.fun2(-5, -5) == 0

def test_fun3():
    assert calculator.fun3(2, 4) == 8
    assert calculator.fun3(0, 5) == 0
    assert calculator.fun3(-1, 5) == -5
    assert calculator.fun3(-3, -2) == 6

def test_fun4():
    assert calculator.fun4(2, 3, 6) == 11
    assert calculator.fun4(5, 1, -1) == 5
    assert calculator.fun4(-2, -2, -2) == -6
    assert calculator.fun4(-3, -2, 100) == 95

def test_fun5():
    assert calculator.fun5(10, 2) == 5
    assert calculator.fun5(5, 2) == 2.5
    assert calculator.fun5(-6, 3) == -2

    with pytest.raises(ZeroDivisionError):
        calculator.fun5(5, 0)

    with pytest.raises(ValueError):
        calculator.fun5("a", 2)

def test_fun6():
    assert calculator.fun6(2) == 4
    assert calculator.fun6(-3) == 9
    assert calculator.fun6(0) == 0
    assert calculator.fun6(2.5) == 6.25

    with pytest.raises(ValueError):
        calculator.fun6("a")


def test_fun7():
    assert calculator.fun7(0) == 1
    assert calculator.fun7(1) == 1
    assert calculator.fun7(5) == 120

    with pytest.raises(ValueError):
        calculator.fun7(-1)

    with pytest.raises(ValueError):
        calculator.fun7(2.5)

def test_fun8():
    assert calculator.fun8(0) == 1
    assert calculator.fun8(1) == 1
    assert calculator.fun8(4) == 24

    with pytest.raises(ValueError):
        calculator.fun8(-3)

    with pytest.raises(ValueError):
        calculator.fun8("5")

def test_fun9():
    assert calculator.fun9(2, 3) == 8
    assert calculator.fun9(5, 0) == 1
    assert calculator.fun9(2, -2) == 0.25
    assert calculator.fun9(2.5, 2) == 6.25

    with pytest.raises(ValueError):
        calculator.fun9("a", 2)

    with pytest.raises(ValueError):
        calculator.fun9(2, 2.5)

def test_fun10():
    assert calculator.fun10(3, 2) == 9
    assert calculator.fun10(10, 1) == 10
    assert calculator.fun10(4, 0) == 1

    with pytest.raises(ValueError):
        calculator.fun10("x", 2)

    with pytest.raises(ValueError):
        calculator.fun10(2, "y")