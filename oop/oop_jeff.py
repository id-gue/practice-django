# Python Classes and Object Oriented Programming / titorial by Jeff Knupp

#  "Classes" and "objects" are often used interchangeably,
#   but they're not really the same thing.
#   Classes = blueprint for creating objects
#   Object = one instance of a class


class Customer(object):
    """A customer of ABC Bank with a checking account."""

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name*
        and starting balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining
        after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after
        depositing *amount* dollars."""
        self.balance += amount
        return self.balance
        

"""
in the shell
    jeff = Customer('Jeff Knupp', 1000.0)
    Customer.withdraw(jeff, 100.0)
"""

# Instance Attributes and Methods


class Car(object):
    # class attribute (doesn't depend on the instance)
    wheels = 4

    def __init__(self, make, model):
        # instance attribute
        self.make = make
        self.model = model

    # static methods don't have access to self
    @staticmethod
    def make_car_sound():
        print("VRoooooooommmm!")

# create instance
mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
# SHELL: 4 wheels on the car instance "Mustang"
print(Car.wheels)
# SHELL: 4 wheels on the Car class


class Vehicle(object):

    # class method = variant of static method,
    # that passed the class instead of receving the instance
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
