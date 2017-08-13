# object oriented programming / tutorial by anandology

# 1__ global state

# simple bank account model
balance = 0


def simple_deposit(amount):
    global balance
    balance += amount
    return balance


def simple_withdraw(amount):
    global balance
    balance -= amount
    return balance

"""
in the shell:
    a = make_account()
    deposit(90)
    withdraw(50)
"""


# reusable bank account model
def make_account():
    return {'balance': 0}


def reusable_deposit(account, amount):
    account['balance'] += amount
    return account['balance']


def reusable_withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

"""
in the shell:
    a = make_account()
    reusable_deposit(a, 100)
    reusable_withdraw(a, 10)
"""


# 2__ Classes and Objects

# simple account
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

"""
in the shell:
    a = BankAccount()
    a.deposit(10)
    a.withdraw(10)
"""

# 3__ Inheritance


# more sophisicated account with minimum balance
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    # overwrites withdraw from BankAccount
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print ('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

"""
in the shell:
    a = MinimumBalanceAccount(10)
    a.deposit(10)
    a.withdraw(10)
"""

# 4__ Special Class Methods


class RationalNumber:
    def __init__(self, nummerator, denominator=1):
        self.n = nummerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * d2 - n2 * d1, d1 * d2)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * n2, d1 * d2)

    def __div__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1 * d2, d1 * n2)

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__
