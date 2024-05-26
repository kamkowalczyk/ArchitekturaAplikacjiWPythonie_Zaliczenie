import pytest
from BankAccount import BankAccount, InvalidAmountError, InsufficientFundsError

def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0

    account_with_initial_balance = BankAccount(100)
    assert account_with_initial_balance.get_balance() == 100

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    with pytest.raises(InvalidAmountError):
        account.deposit(-50)

    with pytest.raises(InvalidAmountError):
        account.deposit(0)

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

    with pytest.raises(InvalidAmountError):
        account.withdraw(-50)

    with pytest.raises(InvalidAmountError):
        account.withdraw(0)

    with pytest.raises(InsufficientFundsError):
        account.withdraw(200)

def test_insufficient_funds():
    account = BankAccount(50)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(100)

def test_combined_operations():
    account = BankAccount()
    account.deposit(200)
    account.withdraw(100)
    assert account.get_balance() == 100

if __name__ == "__main__":
    pytest.main()