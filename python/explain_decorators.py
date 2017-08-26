"""
decorators

decocators add functionality to our function
is function, takes a function, returns a function

@transaction.atomic
@login_required

"""


# write my own decorator
def bold(my_function):
    def inner(*args, **kwargs):
        return '<b>' + my_function(*args, **kwargs) + '</b>'
    return inner


# use my decorator
@bold
def another_function(html):
    return html


# test my decorator
print(another_function('some text'))


# code from ana in Python2
def wrap_it(f):
    def inner(*args, **kwargs):
        return 'bread ' + ' tomato ' + f(*args, **kwargs) + ' lettuce' + ' bread'

    return inner

@wrap_it
def make_sandwich(ingr='ham'):
    return ingr

print make_sandwich()
print make_sandwich('eggs')