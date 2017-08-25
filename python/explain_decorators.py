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
