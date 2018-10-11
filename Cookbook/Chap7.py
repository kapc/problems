#! /usr/env/python

def avg(first, *rest, **kwargs):
    print(first, rest)
    print(rest)
    print(kwargs)

print(avg(1,2,3,[1,2,3],name= 'chandrsh'))

import html

def make_element(name, value, **attr):
    keyvals = ['%s=%s' % item for item in attr.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attr=attr_str, value = html.escape(value))
    return element

def recv(maxsize, *, block):
    pass
recv(1024, block=True)

def minimum(*value, clip=None):
    m = min(*value)
    print(*value)
    print(value)
    if clip is not None:
        m = clip if clip < m else m
    return m

print(minimum([1,2,3,4,5], clip=-120))

def addition(x:int, y:int) -> int:
    return x + y

print(addition.__annotations__)
print(addition(1,2))

b = 1,2
print(b)

def spam(a, b=42):
    print(a)
    print(b)

spam(1)

def spam(a, b=None):
    if b is None:
        b = []

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print("No value is specified for b")

spam(10)

def spam(a, b=[]):
    a = 12
    print(b)
    return b

x = spam(1)
print(x)
x.append(99)
x.append(100)
print(x)
v = spam(1)
print(v)

add = lambda x, y: x + y
print(add(1,20))

def add(x, y):
    return x + y

names = ['Chandresh Kapadia', 'Palak Desai']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

x = 10
a = lambda y : x + y

y = 20
b = lambda y: x + y
print(a(10))
print(b(10))

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x + y

if __name__ == "__main__":
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('TEST')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

# For keeping a state in a call back you can give an object method,
# so basically object can remember state.

class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
p = Pool()

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal  sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler
handler = make_handler()
p.apply_async(add, (5,6), callback=handler)
p.apply_async(add, (5,6), callback=handler)
p.close()
p.join()

class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got : {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import  partial
p = Pool()
p.apply_async(add, (2,3), callback=partial(handler, seq=seq))
p.apply_async(add, (3,3), callback=partial(handler, seq=seq))

p.apply_async(add, (4,5), callback= lambda p: handler(p, seq))
p.close()
p.join()


def test():
    a = yield 1
    b = yield 2
    yield 3

t = test()
z = t.send(None)
print(z)
x = t.send(23)
print(x)
y = t.send(24)
print(y)

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

from functools import wraps

def wrap_func(func):
    @wraps(func)
    def wrapper(*args):
        print("Calling..")
        func(*args)
        print("Calling..")
    return wrapper

@wrap_func
def test():
    print("Called test")

test()

def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(10)
f()
print(f.get_n())

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

c = ClosureInstance()
print(c)

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
s.push(20)
s.push(10)
print(len(s))
print(s.pop())

c = ClosureInstance()
