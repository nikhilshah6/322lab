import pytest
from bank import Account

blah = Account("testing", 10)

def test_initial_balance():
    assert blah.balance == 10

def test_deposit():
    # TODO

def test_withdraw():
    # TODO
