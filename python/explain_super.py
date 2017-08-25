"""
super

used to use functions from the parent class and add some own functions
instead if super yoy could also use the name of the partent class
"""


class Dog(object):
    def speak(self):
        return 'bark!'


# use parent class
class GermanSheperd(Dog):
    pass


# use and change parent class
class Terrier(Dog):
    def speak(self):
        return super().speak() + ' yelp!'


# overwrite parent class
class Husky(Dog):
    def speak(self):
        return 'another sound'

sheperd = GermanSheperd()
print(sheperd.speak())

terrier = Terrier()
print(terrier.speak())

huskey = Husky()
print(huskey.speak())
