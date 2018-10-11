#! /usr/env/python
import time
from functools import wraps

def time_this(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return result
    return wrapper

@time_this
def func_do_nothing(a, b):
    print(a, b)

class A:
    def __init__(self):
        print("chandresh")

    @classmethod
    def method(self):
        print("Inside class method.")

A.method()

func_do_nothing(1,2)
# Preserving metadata when writing decorators.

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("I am called.")
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down.
    :param n:
    :return:
    '''
    print("I am here.")
    while n > 0:
        n -= 1

print(countdown(10000))
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__wrapped__(1000))

from functools import wraps
import logging

def logged(level, name=None, message=None):
    """

    :param level:
    :param name:
    :param message:
    :return:
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log("Inside wrapper")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    print(x + y)


def decorator(x, y=None, z=None):
    def decorate_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(x, y, z)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorate_func


@decorator(1, 2, 3)
def wtf():
    print("What the fuck!")

wtf()

# Attach attributes to wrapper which can be changed at runtime.

from functools import wraps, partial
import logging

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(name)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y
print(add(1,2))

add.set_level(logging.INFO)
print(add(4,5))

# Enforcing type checking


from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorator



# Defining a decorator as a part of the class.
from functools import wraps

class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)
        return wrapper


@A.decorator2
def foo():
    pass

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.nCalls = 0

    def __call__(self, *args, **kwargs):
        self.nCalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y):
    return x + y

print(add)
add(1, 3)
print(add.nCalls)

def profiled(func):
    nCalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal nCalls
        nCalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda : nCalls
    return wrapper

@profiled
def add(x, y):
    return x + y + 100

print(add(1, 2))
print(add(1, 2))
print(add.ncalls())

y = lambda x : "fuck you"
print(y(10))

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r
    return wrapper

class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)

# Writing decorators that add arguments to wrapped functions.
from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@optional_debug
def spam(a, b, c, debug=False):
    print(a, b, c)

spam(1, 2, 3, debug=True)


from functools import wraps
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargsspec(func).args:
        raise TypeError('debug argument already defined.')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper