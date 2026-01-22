# Task 4: Implement a class BankAccount that:
        
# Uses encapsulation for balance (private variable).
# Provides public methods deposit, withdraw, and get_balance.
# Add docstrings to simulate abstraction.

class BankAccount:
    """
    Abstract representation of a bank account.

    This class demonstrates encapsulation by hiding the account balance
    and providing controlled access through public methods.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an initial balance.

        :param initial_balance: Starting amount in the account
        """
        self.__balance = initial_balance  # private variable (encapsulation)

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: Amount to deposit
        """
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient balance exists.

        :param amount: Amount to withdraw
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def get_balance(self):
        """
        Get the current account balance.

        :return: Current balance
        """
        return self.__balance

account = BankAccount(100)
print(account.__doc__)

account.deposit(50)
account.withdraw(30)

print(account.get_balance())
        