# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from Pontellini_002 import BankAccount

@pytest.fixture
def conto():
    return BankAccount("123456789", "Mario Rossi", 1000.0)

def test_get_balance(balance):
    assert balance.get_balance() == 1000.0

def test_deposit(balance):
    balance.deposit(500.0)
    assert balance.get_balance() == 1500.0

def test_withdraw(balance):
    balance.withdraw(200.0)
    assert balance.get_balance() == 800.0

def test_withdraw_insufficient_funds(balance):
    balance.withdraw(2000.0)
    assert balance.get_balance() == 1000.0

def test_deposit_negative_amount(balance):
    balance.deposit(-500.0)
    assert balance.get_balance() == 1000.0