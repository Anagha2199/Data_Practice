import pytest
from wallet import Wallet,InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(100)
    wallet.add_cash(10)
    assert wallet.balance == 110

def test_insufficient_cash():
    wallet = Wallet(100)
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(150)
