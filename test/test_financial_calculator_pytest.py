import pytest
from src.financial_calculator import *

# ---------- Simple Interest Tests ----------

def test_simple_interest_basic():
    assert simple_interest(10000, 5, 2) == 1000


def test_simple_interest_zero_values():
    assert simple_interest(0, 5, 2) == 0
    assert simple_interest(1000, 0, 2) == 0
    assert simple_interest(1000, 5, 0) == 0


def test_simple_interest_invalid():
    with pytest.raises(ValueError):
        simple_interest(-1000, 5, 2)


# ---------- Compound Interest Tests ----------

def test_compound_interest_basic():
    interest = compound_interest(10000, 10, 2, 1)
    assert round(interest, 2) == 2100.00


def test_compound_interest_multiple_frequency():
    interest = compound_interest(10000, 10, 2, 4)
    assert interest > 2100


def test_compound_interest_zero_rate():
    assert compound_interest(10000, 0, 5, 1) == 0


def test_compound_interest_invalid():
    with pytest.raises(ValueError):
        compound_interest(-10000, 5, 2, 1)
    with pytest.raises(ValueError):
        compound_interest(10000, 5, 2, 0)


# ---------- EMI Calculator Tests ----------

def test_calculate_emi_basic():
    emi = calculate_emi(100000, 12, 12)
    assert round(emi, 2) == 8884.88


def test_calculate_emi_zero_interest():
    emi = calculate_emi(120000, 0, 12)
    assert emi == 10000


def test_calculate_emi_invalid():
    with pytest.raises(ValueError):
        calculate_emi(-100000, 10, 12)
    with pytest.raises(ValueError):
        calculate_emi(100000, 10, 0)


# ---------- Profit or Loss Tests ----------

def test_profit_percentage():
    assert profit_or_loss_percentage(100, 150) == 50.0


def test_loss_percentage():
    assert profit_or_loss_percentage(200, 150) == -25.0


def test_profit_or_loss_invalid():
    with pytest.raises(ValueError):
        profit_or_loss_percentage(0, 100)


# ---------- Discounted Price Tests ----------

def test_discounted_price_basic():
    assert discounted_price(2000, 10) == 1800


def test_discounted_price_edge_cases():
    assert discounted_price(1000, 0) == 1000
    assert discounted_price(1000, 100) == 0


def test_discounted_price_invalid():
    with pytest.raises(ValueError):
        discounted_price(-1000, 10)
    with pytest.raises(ValueError):
        discounted_price(1000, 150)