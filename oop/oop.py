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


# 02 reusable bank account model
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
