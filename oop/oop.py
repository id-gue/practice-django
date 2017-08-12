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

# simple class
class BankAccount:
    def __init__(self):
        self.balance = 0

    def class_withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def class_deposit(self, amount):
        self.balance += amount
        return self.balance

"""
in the shell:
    a = BankAccount()
    a.class_deposit(10)
    b.class_withdraw(10)
"""
