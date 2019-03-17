"""
This is closure example
in closure one function return inner function
"""
# def outer_function(name):
#     message = name
#
#     def inner_function():
#         print(message)
#     return inner_function()
#
#
# outer_function("Amir")
# outer_function("Savvy")
"""
Python decorators are functions taking other functions as argument,
add some kind of functionality and returns another function
below is the 1st convestion  1
"""


# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper function executed before {}'.format(original_function.__name__))
#         print('CEO of GOEY.CO')
#         return original_function()
#     return wrapper_function
#
#
# def display():
#     print('Displayed: ' + "Amir Savvy")
#
#
# decorator_display = decorator_function(display)
# decorator_display()


"""
class base decorators

"""


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('__call__ function executed before {}'.format(self.original_function.__name__))
        print('CEO of GOEY.CO')
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('Displayed: ' + "Amir Savvy")


# display()


@DecoratorClass
def display_info(name, age):
    print('display function with agrs ({}, {}): '.format(name, age))


# display_info("Amir Savvy", 26)


"""
Python decorators are functions taking other functions as argument,
add some kind of functionality and returns another function
below is the 2nd convestion  1
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper function executed before {}'.format(original_function.__name__))
        print('CEO of GOEY.CO')
        return original_function(*args, **kwargs)
    return wrapper_function


"""


@decorator_function is the same like: display = decorator_function(display)

"""


@decorator_function
def display():
    print('Displayed: ' + "Amir Savvy")


# display()


"""
display_info is example of args, kwargs example
"""


@decorator_function
def display_info(name, age):
    print('display function with agrs ({}, {}): '.format(name, age))


# display_info("Amir Savvy", 26)


"""
Real example for maintaining script logs using python logging
"""
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))

    return wrapper


"""
calculate running time for any function
"""


def my_timmer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
def display_info(name, age):
    print('display function with agrs ({}, {}): '.format(name, age))


# display_info("Amir", 27)


import time

"""
using multiple decorators to one function is equal,
display_info = my_logger(my_timmer(display_info))
"""


@my_logger
@my_timmer
def display_info(name, age):
    time.sleep(1)
    print('display function with agrs ({}, {}): '.format(name, age))

#
# display_info = my_timmer(display_info)
# print(display_info.__name__)


display_info("Amir Khan", 30)















